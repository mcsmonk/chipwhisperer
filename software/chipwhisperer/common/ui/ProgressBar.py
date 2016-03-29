#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016, NewAE Technology Inc
# All rights reserved.
##
# Find this and more at newae.com - this file is part of the chipwhisperer
# project, http://www.assembla.com/spaces/chipwhisperer
#
#    This file is part of chipwhisperer.
#
#    chipwhisperer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    chipwhisperer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with chipwhisperer.  If not, see <http://www.gnu.org/licenses/>.
#=================================================

from datetime import *


class ProgressBar(object):
    def __init__(self, title = "Progress", textMask ="Initializing...", textValues = None):
        self.title = title
        self.last = self.currentProgress = 0
        self.maximum = 100.0
        self.textMask = textMask
        self.textValues = textValues
        self.startTime = datetime.now()
        self.aborted = False
        self.printAll = False
        print self.title + ": " + self.getText()

    def setText(self, textMask):
        self.textMask = textMask

    def getText(self):
        if self.textValues:
            return self.textMask % self.textValues
        else:
            return self.textMask

    def printStatus(self):
        print self.title + (": %.1f" % ((self.currentProgress/self.maximum) * 100)) + "% (" + self.getText() + ")"

    def updateStatus(self, currentProgress, textValues = None):
        self.textValues = textValues
        self.currentProgress = currentProgress
        if self.printAll or self.currentProgress == 0 or self.currentProgress == self.maximum\
                or self.currentProgress/self.maximum - self.last/self.maximum >= 0.1:
            self.last = currentProgress
            self.printStatus()

    def abort(self):
        self.aborted = True
        print self.title + ": Aborting..."

    def wasAborted(self):
        return self.aborted

    def close(self):
        if not self.wasAborted() and self.currentProgress != self.maximum:
            print self.title + ": Warning, closing before or after 100%: " + "currentProgress = %d and maximum = %d" % (self.currentProgress, self.maximum)

        print self.title + ": Done. Total time = " + (str(datetime.now() - self.startTime))

    def setMaximum(self, value):
        self.maximum = value

    def printAll(self, value):
        self.printAll = value
