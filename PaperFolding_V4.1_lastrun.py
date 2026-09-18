#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on September 17, 2026, at 14:10
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'PaperFolding_V4.1'  # from the Builder filename that created this script
expInfo = {'Participant ID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Participant ID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\SNL General\\Desktop\\Session 2.2\\PaperFolding_V4.1\\PaperFolding_V4.1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instr_slides = visual.ImageStim(
    win=win,
    name='instr_slides', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.6,0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instr_resp = keyboard.Keyboard()
slideN = 1

maxSlideN = 5
minSlideN = 1

# Initialize components for Routine "sample_trial"
sample_trialClock = core.Clock()
sample_image = visual.ImageStim(
    win=win,
    name='sample_image', 
    image='sample_trial.png', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.31),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
sample_resp = keyboard.Keyboard()
sample_txt = visual.TextStim(win=win, name='sample_txt',
    text='Press 1, 2, 3, 4, or 5 on your keyboard.',
    font='Times New Roman',
    pos=(0, -0.36), height=0.038, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "post_sample_instr"
post_sample_instrClock = core.Clock()
post_instr_slides = visual.ImageStim(
    win=win,
    name='post_instr_slides', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.6,0.9),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
post_instr_resp = keyboard.Keyboard()
postslideN = 1

postmaxSlideN = 6
minSlideN = 1

# Initialize components for Routine "test_trial1"
test_trial1Clock = core.Clock()
Questions_1 = visual.ImageStim(
    win=win,
    name='Questions_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
participant_response_1 = keyboard.Keyboard()
resptrial1 = visual.TextStim(win=win, name='resptrial1',
    text='Press 1, 2, 3, 4, or 5 on your keyboard.',
    font='Times New Roman',
    pos=(0, -0.36), height=0.038, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
countdownStarted = False

# Initialize components for Routine "intermission"
intermissionClock = core.Clock()
stop = visual.TextStim(win=win, name='stop',
    text='STOP!',
    font='Times New Roman',
    pos=(0, 0.3), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_part2 = visual.TextStim(win=win, name='start_part2',
    text='You have finished Part I. \n\nWhen you are instructed to begin Part II, press the space bar to continue.\n\nYou will again have 3 minutes to finish Part II.',
    font='Times New Roman',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_response = keyboard.Keyboard()
respbeforetrial2 = visual.TextStim(win=win, name='respbeforetrial2',
    text='When you’re ready to begin, press the space bar to start.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "test_trial2"
test_trial2Clock = core.Clock()
Questions_2 = visual.ImageStim(
    win=win,
    name='Questions_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.6, 0.22),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
participant_response_2 = keyboard.Keyboard()
number = visual.TextStim(win=win, name='number',
    text='Press 1, 2, 3, 4, or 5 on your keyboard.',
    font='Times New Roman',
    pos=(0, -0.36), height=0.038, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "end"
endClock = core.Clock()
thankyou = visual.TextStim(win=win, name='thankyou',
    text='You have now completed the experiment. \n\nThank you for your participation!',
    font='Times New Roman',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
final = keyboard.Keyboard()
finalslide = visual.TextStim(win=win, name='finalslide',
    text='Press the space bar to exit the experiment.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instr_images = data.TrialHandler(nReps=1000.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instr_images')
thisExp.addLoop(instr_images)  # add the loop to the experiment
thisInstr_image = instr_images.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstr_image.rgb)
if thisInstr_image != None:
    for paramName in thisInstr_image:
        exec('{} = thisInstr_image[paramName]'.format(paramName))

for thisInstr_image in instr_images:
    currentLoop = instr_images
    # abbreviate parameter names if possible (e.g. rgb = thisInstr_image.rgb)
    if thisInstr_image != None:
        for paramName in thisInstr_image:
            exec('{} = thisInstr_image[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    instr_slides.setImage('paperfolding_instr/Slide' + str(slideN) + '.png')
    instr_resp.keys = []
    instr_resp.rt = []
    _instr_resp_allKeys = []
    # keep track of which components have finished
    instrComponents = [instr_slides, instr_resp]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_slides* updates
        if instr_slides.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_slides.frameNStart = frameN  # exact frame index
            instr_slides.tStart = t  # local t and not account for scr refresh
            instr_slides.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_slides, 'tStartRefresh')  # time at next scr refresh
            instr_slides.setAutoDraw(True)
        
        # *instr_resp* updates
        waitOnFlip = False
        if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            instr_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_resp.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _instr_resp_allKeys.extend(theseKeys)
            if len(_instr_resp_allKeys):
                instr_resp.keys = _instr_resp_allKeys[-1].name  # just the last key pressed
                instr_resp.rt = _instr_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instr_images.addData('instr_slides.started', instr_slides.tStartRefresh)
    instr_images.addData('instr_slides.stopped', instr_slides.tStopRefresh)
    if instr_resp.keys == 'left':
        slideN -= 1
    elif instr_resp.keys == 'right':
        slideN += 1
    elif instr_resp.keys == 'space':
        if slideN == maxSlideN:
            instr_images.finished = True
    
    if slideN > maxSlideN:
        slideN = maxSlideN
    if slideN < minSlideN:
        slideN = minSlideN
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1000.0 repeats of 'instr_images'


# ------Prepare to start Routine "sample_trial"-------
continueRoutine = True
# update component parameters for each repeat
sample_resp.keys = []
sample_resp.rt = []
_sample_resp_allKeys = []
# keep track of which components have finished
sample_trialComponents = [sample_image, sample_resp, sample_txt]
for thisComponent in sample_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sample_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sample_trial"-------
while continueRoutine:
    # get current time
    t = sample_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sample_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sample_image* updates
    if sample_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sample_image.frameNStart = frameN  # exact frame index
        sample_image.tStart = t  # local t and not account for scr refresh
        sample_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sample_image, 'tStartRefresh')  # time at next scr refresh
        sample_image.setAutoDraw(True)
    
    # *sample_resp* updates
    waitOnFlip = False
    if sample_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sample_resp.frameNStart = frameN  # exact frame index
        sample_resp.tStart = t  # local t and not account for scr refresh
        sample_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sample_resp, 'tStartRefresh')  # time at next scr refresh
        sample_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sample_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sample_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sample_resp.status == STARTED and not waitOnFlip:
        theseKeys = sample_resp.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
        _sample_resp_allKeys.extend(theseKeys)
        if len(_sample_resp_allKeys):
            sample_resp.keys = _sample_resp_allKeys[-1].name  # just the last key pressed
            sample_resp.rt = _sample_resp_allKeys[-1].rt
            # was this correct?
            if (sample_resp.keys == str('3')) or (sample_resp.keys == '3'):
                sample_resp.corr = 1
            else:
                sample_resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # *sample_txt* updates
    if sample_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sample_txt.frameNStart = frameN  # exact frame index
        sample_txt.tStart = t  # local t and not account for scr refresh
        sample_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sample_txt, 'tStartRefresh')  # time at next scr refresh
        sample_txt.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sample_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sample_trial"-------
for thisComponent in sample_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sample_image.started', sample_image.tStartRefresh)
thisExp.addData('sample_image.stopped', sample_image.tStopRefresh)
# check responses
if sample_resp.keys in ['', [], None]:  # No response was made
    sample_resp.keys = None
    # was no response the correct answer?!
    if str('3').lower() == 'none':
       sample_resp.corr = 1;  # correct non-response
    else:
       sample_resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('sample_resp.keys',sample_resp.keys)
thisExp.addData('sample_resp.corr', sample_resp.corr)
if sample_resp.keys != None:  # we had a response
    thisExp.addData('sample_resp.rt', sample_resp.rt)
thisExp.addData('sample_resp.started', sample_resp.tStartRefresh)
thisExp.addData('sample_resp.stopped', sample_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('sample_txt.started', sample_txt.tStartRefresh)
thisExp.addData('sample_txt.stopped', sample_txt.tStopRefresh)
# the Routine "sample_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
post_sample_instr_images = data.TrialHandler(nReps=1000.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='post_sample_instr_images')
thisExp.addLoop(post_sample_instr_images)  # add the loop to the experiment
thisPost_sample_instr_image = post_sample_instr_images.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPost_sample_instr_image.rgb)
if thisPost_sample_instr_image != None:
    for paramName in thisPost_sample_instr_image:
        exec('{} = thisPost_sample_instr_image[paramName]'.format(paramName))

for thisPost_sample_instr_image in post_sample_instr_images:
    currentLoop = post_sample_instr_images
    # abbreviate parameter names if possible (e.g. rgb = thisPost_sample_instr_image.rgb)
    if thisPost_sample_instr_image != None:
        for paramName in thisPost_sample_instr_image:
            exec('{} = thisPost_sample_instr_image[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "post_sample_instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    post_instr_slides.setImage('paperfolding_post_instr/Slide' + str(postslideN) + '.png')
    post_instr_resp.keys = []
    post_instr_resp.rt = []
    _post_instr_resp_allKeys = []
    # keep track of which components have finished
    post_sample_instrComponents = [post_instr_slides, post_instr_resp]
    for thisComponent in post_sample_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    post_sample_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "post_sample_instr"-------
    while continueRoutine:
        # get current time
        t = post_sample_instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=post_sample_instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *post_instr_slides* updates
        if post_instr_slides.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            post_instr_slides.frameNStart = frameN  # exact frame index
            post_instr_slides.tStart = t  # local t and not account for scr refresh
            post_instr_slides.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_instr_slides, 'tStartRefresh')  # time at next scr refresh
            post_instr_slides.setAutoDraw(True)
        
        # *post_instr_resp* updates
        waitOnFlip = False
        if post_instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            post_instr_resp.frameNStart = frameN  # exact frame index
            post_instr_resp.tStart = t  # local t and not account for scr refresh
            post_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(post_instr_resp, 'tStartRefresh')  # time at next scr refresh
            post_instr_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(post_instr_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(post_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if post_instr_resp.status == STARTED and not waitOnFlip:
            theseKeys = post_instr_resp.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
            _post_instr_resp_allKeys.extend(theseKeys)
            if len(_post_instr_resp_allKeys):
                post_instr_resp.keys = _post_instr_resp_allKeys[-1].name  # just the last key pressed
                post_instr_resp.rt = _post_instr_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in post_sample_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "post_sample_instr"-------
    for thisComponent in post_sample_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    post_sample_instr_images.addData('post_instr_slides.started', post_instr_slides.tStartRefresh)
    post_sample_instr_images.addData('post_instr_slides.stopped', post_instr_slides.tStopRefresh)
    if post_instr_resp.keys == 'left':
        postslideN -= 1
    elif post_instr_resp.keys == 'right':
        postslideN += 1
    elif post_instr_resp.keys == 'space':
        if postslideN == postmaxSlideN:
            post_sample_instr_images.finished = True
    
    if postslideN > postmaxSlideN:
        postslideN = postmaxSlideN
    if postslideN < minSlideN:
        postslideN = minSlideN
    # the Routine "post_sample_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1000.0 repeats of 'post_sample_instr_images'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_and_corrAns_Part_1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "test_trial1"-------
    continueRoutine = True
    # update component parameters for each repeat
    Questions_1.setImage(ImageFile)
    participant_response_1.keys = []
    participant_response_1.rt = []
    _participant_response_1_allKeys = []
    #Setting Clock
    if not countdownStarted:
        countdownClock = core.CountdownTimer(180.0)
        countdownStarted = True
    # keep track of which components have finished
    test_trial1Components = [Questions_1, participant_response_1, resptrial1]
    for thisComponent in test_trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test_trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test_trial1"-------
    while continueRoutine:
        # get current time
        t = test_trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test_trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Questions_1* updates
        if Questions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Questions_1.frameNStart = frameN  # exact frame index
            Questions_1.tStart = t  # local t and not account for scr refresh
            Questions_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Questions_1, 'tStartRefresh')  # time at next scr refresh
            Questions_1.setAutoDraw(True)
        
        # *participant_response_1* updates
        waitOnFlip = False
        if participant_response_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            participant_response_1.frameNStart = frameN  # exact frame index
            participant_response_1.tStart = t  # local t and not account for scr refresh
            participant_response_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(participant_response_1, 'tStartRefresh')  # time at next scr refresh
            participant_response_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(participant_response_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(participant_response_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if participant_response_1.status == STARTED and not waitOnFlip:
            theseKeys = participant_response_1.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _participant_response_1_allKeys.extend(theseKeys)
            if len(_participant_response_1_allKeys):
                participant_response_1.keys = _participant_response_1_allKeys[0].name  # just the first key pressed
                participant_response_1.rt = _participant_response_1_allKeys[0].rt
                # was this correct?
                if (participant_response_1.keys == str(corrAns)) or (participant_response_1.keys == corrAns):
                    participant_response_1.corr = 1
                else:
                    participant_response_1.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *resptrial1* updates
        if resptrial1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resptrial1.frameNStart = frameN  # exact frame index
            resptrial1.tStart = t  # local t and not account for scr refresh
            resptrial1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resptrial1, 'tStartRefresh')  # time at next scr refresh
            resptrial1.setAutoDraw(True)
        #Establishing and Displaying Timer
        timeRemaining = countdownClock.getTime()
        if timeRemaining <=0.00:
            continueRoutine = False
            trials.finished = True
            countdownStarted = False
            continueExperiment = True
        else:
            minutes = int (timeRemaining/60.00)
            seconds = int (timeRemaining - (minutes*60.00))
            timeText = str(minutes) + ':'  + str(seconds) 
        
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_trial1"-------
    for thisComponent in test_trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Questions_1.started', Questions_1.tStartRefresh)
    trials.addData('Questions_1.stopped', Questions_1.tStopRefresh)
    # check responses
    if participant_response_1.keys in ['', [], None]:  # No response was made
        participant_response_1.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           participant_response_1.corr = 1;  # correct non-response
        else:
           participant_response_1.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('participant_response_1.keys',participant_response_1.keys)
    trials.addData('participant_response_1.corr', participant_response_1.corr)
    if participant_response_1.keys != None:  # we had a response
        trials.addData('participant_response_1.rt', participant_response_1.rt)
    trials.addData('participant_response_1.started', participant_response_1.tStartRefresh)
    trials.addData('participant_response_1.stopped', participant_response_1.tStopRefresh)
    trials.addData('resptrial1.started', resptrial1.tStartRefresh)
    trials.addData('resptrial1.stopped', resptrial1.tStopRefresh)
    # the Routine "test_trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "intermission"-------
continueRoutine = True
# update component parameters for each repeat
key_response.keys = []
key_response.rt = []
_key_response_allKeys = []
# keep track of which components have finished
intermissionComponents = [stop, start_part2, key_response, respbeforetrial2]
for thisComponent in intermissionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intermissionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intermission"-------
while continueRoutine:
    # get current time
    t = intermissionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intermissionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *stop* updates
    if stop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stop.frameNStart = frameN  # exact frame index
        stop.tStart = t  # local t and not account for scr refresh
        stop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stop, 'tStartRefresh')  # time at next scr refresh
        stop.setAutoDraw(True)
    
    # *start_part2* updates
    if start_part2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_part2.frameNStart = frameN  # exact frame index
        start_part2.tStart = t  # local t and not account for scr refresh
        start_part2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_part2, 'tStartRefresh')  # time at next scr refresh
        start_part2.setAutoDraw(True)
    
    # *key_response* updates
    waitOnFlip = False
    if key_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_response.frameNStart = frameN  # exact frame index
        key_response.tStart = t  # local t and not account for scr refresh
        key_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
        key_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_response.status == STARTED and not waitOnFlip:
        theseKeys = key_response.getKeys(keyList=['space'], waitRelease=False)
        _key_response_allKeys.extend(theseKeys)
        if len(_key_response_allKeys):
            key_response.keys = _key_response_allKeys[-1].name  # just the last key pressed
            key_response.rt = _key_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *respbeforetrial2* updates
    if respbeforetrial2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respbeforetrial2.frameNStart = frameN  # exact frame index
        respbeforetrial2.tStart = t  # local t and not account for scr refresh
        respbeforetrial2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respbeforetrial2, 'tStartRefresh')  # time at next scr refresh
        respbeforetrial2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intermissionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intermission"-------
for thisComponent in intermissionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stop.started', stop.tStartRefresh)
thisExp.addData('stop.stopped', stop.tStopRefresh)
thisExp.addData('start_part2.started', start_part2.tStartRefresh)
thisExp.addData('start_part2.stopped', start_part2.tStopRefresh)
thisExp.addData('respbeforetrial2.started', respbeforetrial2.tStartRefresh)
thisExp.addData('respbeforetrial2.stopped', respbeforetrial2.tStopRefresh)
myClock = core.Clock()
# the Routine "intermission" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_and_corrAns_Part_2.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "test_trial2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Questions_2.setImage(ImageFile)
    participant_response_2.keys = []
    participant_response_2.rt = []
    _participant_response_2_allKeys = []
    # keep track of which components have finished
    test_trial2Components = [Questions_2, participant_response_2, number]
    for thisComponent in test_trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    test_trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test_trial2"-------
    while continueRoutine:
        # get current time
        t = test_trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=test_trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Questions_2* updates
        if Questions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Questions_2.frameNStart = frameN  # exact frame index
            Questions_2.tStart = t  # local t and not account for scr refresh
            Questions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Questions_2, 'tStartRefresh')  # time at next scr refresh
            Questions_2.setAutoDraw(True)
        
        # *participant_response_2* updates
        waitOnFlip = False
        if participant_response_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            participant_response_2.frameNStart = frameN  # exact frame index
            participant_response_2.tStart = t  # local t and not account for scr refresh
            participant_response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(participant_response_2, 'tStartRefresh')  # time at next scr refresh
            participant_response_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(participant_response_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(participant_response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if participant_response_2.status == STARTED and not waitOnFlip:
            theseKeys = participant_response_2.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _participant_response_2_allKeys.extend(theseKeys)
            if len(_participant_response_2_allKeys):
                participant_response_2.keys = _participant_response_2_allKeys[0].name  # just the first key pressed
                participant_response_2.rt = _participant_response_2_allKeys[0].rt
                # was this correct?
                if (participant_response_2.keys == str(corrAns)) or (participant_response_2.keys == corrAns):
                    participant_response_2.corr = 1
                else:
                    participant_response_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *number* updates
        if number.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            number.frameNStart = frameN  # exact frame index
            number.tStart = t  # local t and not account for scr refresh
            number.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(number, 'tStartRefresh')  # time at next scr refresh
            number.setAutoDraw(True)
        ##Creating Clock
        #timeRemaining = countdownClock.getTime()
        #if timeRemaining <=0.00:
        #    continueRoutine = False
        #    trials2.finished = True
        #    countdownStarted = False
        #    continueExperiment = True
        #else:
        #    minutes = int (timeRemaining/60.00)
        #    seconds = int (timeRemaining - (minutes*60.00))
        #    timeText = str(minutes) + ':'  + str(seconds) 
        
        threshold = 180
        time = myClock.getTime()
        
        if time > threshold:
            continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test_trial2"-------
    for thisComponent in test_trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('Questions_2.started', Questions_2.tStartRefresh)
    trials_2.addData('Questions_2.stopped', Questions_2.tStopRefresh)
    # check responses
    if participant_response_2.keys in ['', [], None]:  # No response was made
        participant_response_2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           participant_response_2.corr = 1;  # correct non-response
        else:
           participant_response_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('participant_response_2.keys',participant_response_2.keys)
    trials_2.addData('participant_response_2.corr', participant_response_2.corr)
    if participant_response_2.keys != None:  # we had a response
        trials_2.addData('participant_response_2.rt', participant_response_2.rt)
    trials_2.addData('participant_response_2.started', participant_response_2.tStartRefresh)
    trials_2.addData('participant_response_2.stopped', participant_response_2.tStopRefresh)
    trials_2.addData('number.started', number.tStartRefresh)
    trials_2.addData('number.stopped', number.tStopRefresh)
    # the Routine "test_trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
final.keys = []
final.rt = []
_final_allKeys = []
# keep track of which components have finished
endComponents = [thankyou, final, finalslide]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thankyou* updates
    if thankyou.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thankyou.frameNStart = frameN  # exact frame index
        thankyou.tStart = t  # local t and not account for scr refresh
        thankyou.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thankyou, 'tStartRefresh')  # time at next scr refresh
        thankyou.setAutoDraw(True)
    
    # *final* updates
    waitOnFlip = False
    if final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        final.frameNStart = frameN  # exact frame index
        final.tStart = t  # local t and not account for scr refresh
        final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(final, 'tStartRefresh')  # time at next scr refresh
        final.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(final.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(final.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if final.status == STARTED and not waitOnFlip:
        theseKeys = final.getKeys(keyList=['space'], waitRelease=False)
        _final_allKeys.extend(theseKeys)
        if len(_final_allKeys):
            final.keys = _final_allKeys[-1].name  # just the last key pressed
            final.rt = _final_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *finalslide* updates
    if finalslide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalslide.frameNStart = frameN  # exact frame index
        finalslide.tStart = t  # local t and not account for scr refresh
        finalslide.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalslide, 'tStartRefresh')  # time at next scr refresh
        finalslide.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thankyou.started', thankyou.tStartRefresh)
thisExp.addData('thankyou.stopped', thankyou.tStopRefresh)
# check responses
if final.keys in ['', [], None]:  # No response was made
    final.keys = None
thisExp.addData('final.keys',final.keys)
if final.keys != None:  # we had a response
    thisExp.addData('final.rt', final.rt)
thisExp.addData('final.started', final.tStartRefresh)
thisExp.addData('final.stopped', final.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('finalslide.started', finalslide.tStartRefresh)
thisExp.addData('finalslide.stopped', finalslide.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
