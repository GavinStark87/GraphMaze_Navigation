#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Graph Maze Navigation Task -- MAIN TASK
MenoMaps Project - UC Irvine Spatial Neuroscience Lab

Run after GraphMaze_Practice.py has been completed.
Contains brick main trials and hedge main trials only -- no practice, no feedback.
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os, sys
from psychopy.hardware import keyboard

# -- Paths -------------------------------------------------------------------
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

data_dir = os.path.join(_thisDir, 'data')
if not os.path.isdir(data_dir):
    os.makedirs(data_dir)

# -- Experiment Info ---------------------------------------------------------
psychopyVersion = '2021.2.3'
expName = 'GraphMaze_Navigation'
expInfo = {'Participant ID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (
    expInfo['Participant ID'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=_thisDir,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename + '.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001

# -- Window ------------------------------------------------------------------
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] is not None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()

# -- Colors ------------------------------------------------------------------
COLOR_BLACK = [0, 0, 0]
COLOR_BLUE  = [0.2, 0.55, 0.95]     # lighter blue -- path distance trials
COLOR_PEACH = [0.914, 0.506, 0.090] # peach        -- straight-line trials

# -- Question text map -------------------------------------------------------
question_map = {
    'route': 'Which is the shortest path distance from the start?',
    'line':  'Which is the shortest straight-line distance from the start?'
}

# -- Ready slide text --------------------------------------------------------
# Update trial count here if boss confirms final CSV sizes differ from 200.
SLIDE_READY_BODY = (
    "You will now begin the main task. There will be a total of 200 trials across "
    "the two environments you have learned.\n\n"
    "You will have 10 seconds to respond to each trial. "
    "You will not be given feedback on your performance.\n\n"
    "As a reminder, indicate which object is closer to your starting point "
    "via shortest path distance (blue) or shortest straight-line distance (peach) -- "
    "they may not be the same answer!\n\n"
    "Do you have any questions?"
)

# -- Global Timers -----------------------------------------------------------
globalClock = core.Clock()
routineTimer = core.CountdownTimer()

# ===========================================================================
# VISUAL COMPONENTS
# ===========================================================================

# Fixation cross
fixClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+', font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=0.0)

# Environment label -- large centered text, no maze image
envClock = core.Clock()
env_label = visual.TextStim(win=win, name='env_label',
    text='', font='Arial',
    pos=(0, 0), height=0.14, wrapWidth=1.4, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=0.0)
env_advance = visual.TextStim(win=win, name='env_advance',
    text='Press 5 to continue.',
    font='Arial', pos=(0, -0.46), height=0.038, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=-1.0)

# Trial components (black text on colored backgrounds)
trialClock = core.Clock()

question_text = visual.TextStim(win=win, name='question_text',
    text='', font='Arial',
    pos=(0, 0.40), height=0.055, wrapWidth=1.5, ori=0,
    color='black', colorSpace='rgb', opacity=1, depth=0.0)

cue_image = visual.ImageStim(
    win=win, name='cue_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0.12), size=(0.25, 0.25),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

cue_label_stim = visual.TextStim(win=win, name='cue_label_stim',
    text='', font='Arial',
    pos=(0, -0.02), height=0.042, wrapWidth=0.5, ori=0,
    color='black', colorSpace='rgb', opacity=1, depth=-2.0)

left_image = visual.ImageStim(
    win=win, name='left_image',
    image='sin', mask=None,
    ori=0, pos=(-0.22, -0.22), size=(0.22, 0.22),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)

left_label_stim = visual.TextStim(win=win, name='left_label_stim',
    text='', font='Arial',
    pos=(-0.22, -0.36), height=0.042, wrapWidth=0.35, ori=0,
    color='black', colorSpace='rgb', opacity=1, depth=-4.0)

right_image = visual.ImageStim(
    win=win, name='right_image',
    image='sin', mask=None,
    ori=0, pos=(0.22, -0.22), size=(0.22, 0.22),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)

right_label_stim = visual.TextStim(win=win, name='right_label_stim',
    text='', font='Arial',
    pos=(0.22, -0.36), height=0.042, wrapWidth=0.35, ori=0,
    color='black', colorSpace='rgb', opacity=1, depth=-6.0)

trial_resp = keyboard.Keyboard()

# End screen
endClock = core.Clock()
thankyou = visual.TextStim(win=win, name='thankyou',
    text='You have now completed the experiment.\n\nThank you for your participation!',
    font='Arial', pos=(0, 0.1), height=0.06, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=0.0)
finalslide = visual.TextStim(win=win, name='finalslide',
    text='Press 5 to exit.',
    font='Arial', pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=-1.0)
final_key = keyboard.Keyboard()

# ===========================================================================
# HELPER FUNCTIONS
# ===========================================================================

def load_conditions(csv_path):
    """Load a conditions CSV, quitting with a clear message if not found."""
    if not os.path.isfile(csv_path):
        print('ERROR: conditions file not found: ' + csv_path)
        print('Expected location: ' + os.path.join(_thisDir, csv_path))
        win.close()
        core.quit()
    try:
        return data.importConditions(csv_path)
    except Exception as e:
        print('ERROR: failed to read ' + csv_path)
        print(str(e))
        win.close()
        core.quit()


def show_fixation(duration=1.0):
    """Display fixation cross for a fixed duration on black background."""
    win.color = COLOR_BLACK
    routineTimer.reset()
    routineTimer.add(duration)
    fixation.status = NOT_STARTED
    fixation.tStart = None
    _timeToFirstFrame = win.getFutureFlipTime(clock='now')
    fixClock.reset(-_timeToFirstFrame)
    frameN = -1
    while routineTimer.getTime() > 0:
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            fixation.frameNStart = frameN
            fixation.tStart = fixClock.getTime()
            fixation.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(fixation, 'tStartRefresh')
            fixation.setAutoDraw(True)
        if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
            core.quit()
        win.flip()
    fixation.setAutoDraw(False)
    routineTimer.reset()


def show_text_slide(body_text):
    """
    Display a text-only ready slide on a black background.
    Key 5 to advance. No title, no color hints.
    """
    win.color = COLOR_BLACK
    slideClock = core.Clock()

    body_stim = visual.TextStim(win,
        text=body_text, font='Arial',
        pos=(0, 0.08), height=0.036,
        wrapWidth=1.5, color='white', colorSpace='rgb',
        depth=-1.0)
    advance_stim = visual.TextStim(win,
        text='Press 5 to begin.',
        font='Arial', pos=(0, -0.47), height=0.031,
        color=[0.4, 0.4, 0.4], colorSpace='rgb', depth=-2.0)
    vis_comps = [body_stim, advance_stim]

    slide_resp = keyboard.Keyboard()
    for comp in vis_comps:
        comp.status = NOT_STARTED
        comp.tStart = None
    slide_resp.status = NOT_STARTED
    slide_resp.keys = []
    _allKeys = []
    continueRoutine = True
    _timeToFirstFrame = win.getFutureFlipTime(clock='now')
    slideClock.reset(-_timeToFirstFrame)
    frameN = -1

    while continueRoutine:
        tThisFlip = win.getFutureFlipTime(clock=slideClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        for comp in vis_comps:
            if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                comp.frameNStart = frameN
                comp.tStart = slideClock.getTime()
                comp.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(comp, 'tStartRefresh')
                comp.setAutoDraw(True)
        waitOnFlip = False
        if slide_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            slide_resp.frameNStart = frameN
            slide_resp.tStart = slideClock.getTime()
            slide_resp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(slide_resp, 'tStartRefresh')
            slide_resp.status = STARTED
            waitOnFlip = True
            win.callOnFlip(slide_resp.clock.reset)
            win.callOnFlip(slide_resp.clearEvents, eventType='keyboard')
        if slide_resp.status == STARTED and not waitOnFlip:
            theseKeys = slide_resp.getKeys(keyList=['5'], waitRelease=False)
            _allKeys.extend(theseKeys)
            if len(_allKeys):
                continueRoutine = False
        if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
            core.quit()
        if continueRoutine:
            win.flip()

    for comp in vis_comps:
        comp.setAutoDraw(False)
    routineTimer.reset()


def show_env_label(label_text):
    """
    Display environment name as large centered text on black background.
    No maze image. Key 5 to advance.
    """
    win.color = COLOR_BLACK
    env_label.setText(label_text)
    display_comps = [env_label, env_advance]

    env_resp = keyboard.Keyboard()
    for comp in display_comps:
        comp.status = NOT_STARTED
        comp.tStart = None
    env_resp.status = NOT_STARTED
    env_resp.keys = []
    _allKeys = []
    continueRoutine = True
    _timeToFirstFrame = win.getFutureFlipTime(clock='now')
    envClock.reset(-_timeToFirstFrame)
    frameN = -1

    while continueRoutine:
        tThisFlip = win.getFutureFlipTime(clock=envClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        for comp in display_comps:
            if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                comp.frameNStart = frameN
                comp.tStart = envClock.getTime()
                comp.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(comp, 'tStartRefresh')
                comp.setAutoDraw(True)
        waitOnFlip = False
        if env_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            env_resp.frameNStart = frameN
            env_resp.tStart = envClock.getTime()
            env_resp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(env_resp, 'tStartRefresh')
            env_resp.status = STARTED
            waitOnFlip = True
            win.callOnFlip(env_resp.clock.reset)
            win.callOnFlip(env_resp.clearEvents, eventType='keyboard')
        if env_resp.status == STARTED and not waitOnFlip:
            theseKeys = env_resp.getKeys(keyList=['5'], waitRelease=False)
            _allKeys.extend(theseKeys)
            if len(_allKeys):
                continueRoutine = False
        if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
            core.quit()
        if continueRoutine:
            win.flip()

    for comp in display_comps:
        comp.setAutoDraw(False)
    routineTimer.reset()


def run_trial(trialData):
    """
    Run one main trial (no feedback). Returns (keys, rt, corr).
    Background: blue for route, peach for line.
    Key map: 1 = left, 2 = right.
    core.CountdownTimer(10) ends trial after 10 seconds if no response.
    """
    trial_type = trialData['trial_type']
    win.color = COLOR_BLUE if trial_type == 'route' else COLOR_PEACH

    cue_image.setImage(trialData['cueImage'])
    left_image.setImage(trialData['leftImage'])
    right_image.setImage(trialData['rightImage'])
    cue_label_stim.setText(trialData['cueLabel'])
    left_label_stim.setText(trialData['leftLabel'])
    right_label_stim.setText(trialData['rightLabel'])
    question_text.setText(question_map.get(trial_type, 'Which object is closer?'))

    trial_resp.keys = []
    trial_resp.rt = []
    _trial_allKeys = []

    vis_comps = [question_text, cue_image, cue_label_stim,
                 left_image, left_label_stim,
                 right_image, right_label_stim]
    for comp in vis_comps + [trial_resp]:
        comp.tStart = None
        comp.tStop = None
        comp.tStartRefresh = None
        comp.tStopRefresh = None
        if hasattr(comp, 'status'):
            comp.status = NOT_STARTED

    trialCountdown = core.CountdownTimer(10)

    continueRoutine = True
    _timeToFirstFrame = win.getFutureFlipTime(clock='now')
    trialClock.reset(-_timeToFirstFrame)
    frameN = -1

    while continueRoutine:
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        for comp in vis_comps:
            if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                comp.frameNStart = frameN
                comp.tStart = trialClock.getTime()
                comp.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(comp, 'tStartRefresh')
                comp.setAutoDraw(True)

        waitOnFlip = False
        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            trial_resp.frameNStart = frameN
            trial_resp.tStart = trialClock.getTime()
            trial_resp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(trial_resp, 'tStartRefresh')
            trial_resp.status = STARTED
            waitOnFlip = True
            win.callOnFlip(trial_resp.clock.reset)
            win.callOnFlip(trial_resp.clearEvents, eventType='keyboard')

        if trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_resp.getKeys(keyList=['1', '2'], waitRelease=False)
            _trial_allKeys.extend(theseKeys)
            if len(_trial_allKeys):
                trial_resp.keys = _trial_allKeys[0].name
                trial_resp.rt   = _trial_allKeys[0].rt
                key_map = {'1': 'left', '2': 'right'}
                response_dir = key_map.get(trial_resp.keys, trial_resp.keys)
                if (response_dir == str(trialData['corrAns']) or
                        response_dir == trialData['corrAns']):
                    trial_resp.corr = 1
                else:
                    trial_resp.corr = 0
                continueRoutine = False

        if trialCountdown.getTime() <= 0:
            continueRoutine = False

        if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
            core.quit()
        if continueRoutine:
            win.flip()

    for comp in vis_comps:
        comp.setAutoDraw(False)

    if trial_resp.keys in ['', [], None]:
        trial_resp.keys = None
        trial_resp.rt   = None
        trial_resp.corr = 0

    win.color = COLOR_BLACK
    return trial_resp.keys, trial_resp.rt, trial_resp.corr


# ===========================================================================
# EXPERIMENT FLOW
# ===========================================================================

# 1. Ready slide (brief reminder + questions check)
show_text_slide(SLIDE_READY_BODY)

# ---------------------------------------------------------------------------
# BRICK main trials (randomised, no feedback)
# ---------------------------------------------------------------------------
show_env_label('Brick Maze')

brick_trials = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=load_conditions('nav_task_conditions_brick.csv'),
    seed=None, name='brick_trials')
thisExp.addLoop(brick_trials)

for thisTrial in brick_trials:
    currentLoop = brick_trials
    if thisTrial is not None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    show_fixation(1.0)
    respKeys, respRT, respCorr = run_trial(thisTrial)

    brick_trials.addData('trial_resp.keys', respKeys)
    brick_trials.addData('trial_resp.corr', respCorr)
    if respKeys is not None:
        brick_trials.addData('trial_resp.rt', respRT)
    brick_trials.addData('trial_type', thisTrial['trial_type'])
    brick_trials.addData('cue_image.file', thisTrial['cueImage'])
    brick_trials.addData('left_image.file', thisTrial['leftImage'])
    brick_trials.addData('right_image.file', thisTrial['rightImage'])

    routineTimer.reset()
    thisExp.nextEntry()

event.clearEvents()
defaultKeyboard.clearEvents()

# ---------------------------------------------------------------------------
# HEDGE main trials (randomised, no feedback)
# ---------------------------------------------------------------------------
show_env_label('Hedge Maze')

hedge_trials = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=load_conditions('nav_task_conditions.csv'),
    seed=None, name='hedge_trials')
thisExp.addLoop(hedge_trials)

for thisTrial in hedge_trials:
    currentLoop = hedge_trials
    if thisTrial is not None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    show_fixation(1.0)
    respKeys, respRT, respCorr = run_trial(thisTrial)

    hedge_trials.addData('trial_resp.keys', respKeys)
    hedge_trials.addData('trial_resp.corr', respCorr)
    if respKeys is not None:
        hedge_trials.addData('trial_resp.rt', respRT)
    hedge_trials.addData('trial_type', thisTrial['trial_type'])
    hedge_trials.addData('cue_image.file', thisTrial['cueImage'])
    hedge_trials.addData('left_image.file', thisTrial['leftImage'])
    hedge_trials.addData('right_image.file', thisTrial['rightImage'])

    routineTimer.reset()
    thisExp.nextEntry()

# Save per-environment trial files
for handler, label in [(brick_trials, 'brick'), (hedge_trials, 'hedge')]:
    if handler.trialList not in ([], [None], None):
        params = handler.trialList[0].keys()
    else:
        params = []
    handler.saveAsText(filename + label + '_trials.csv', delim=',',
        stimOut=params,
        dataOut=['n', 'all_mean', 'all_std', 'all_raw'])

# ===========================================================================
# END SCREEN
# ===========================================================================
win.color = COLOR_BLACK
continueRoutine = True
final_key.keys = []
final_key.rt = []
_final_allKeys = []

endComponents = [thankyou, final_key, finalslide]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
_timeToFirstFrame = win.getFutureFlipTime(clock='now')
endClock.reset(-_timeToFirstFrame)
frameN = -1

while continueRoutine:
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    for comp in [thankyou, finalslide]:
        if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            comp.frameNStart = frameN
            comp.tStart = endClock.getTime()
            comp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(comp, 'tStartRefresh')
            comp.setAutoDraw(True)
    waitOnFlip = False
    if final_key.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        final_key.frameNStart = frameN
        final_key.tStart = endClock.getTime()
        final_key.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(final_key, 'tStartRefresh')
        final_key.status = STARTED
        waitOnFlip = True
        win.callOnFlip(final_key.clock.reset)
        win.callOnFlip(final_key.clearEvents, eventType='keyboard')
    if final_key.status == STARTED and not waitOnFlip:
        theseKeys = final_key.getKeys(keyList=['5'], waitRelease=False)
        _final_allKeys.extend(theseKeys)
        if len(_final_allKeys):
            final_key.keys = _final_allKeys[-1].name
            final_key.rt   = _final_allKeys[-1].rt
            continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
        core.quit()
    if continueRoutine:
        win.flip()

for comp in [thankyou, finalslide]:
    comp.setAutoDraw(False)
if final_key.keys in ['', [], None]:
    final_key.keys = None
thisExp.addData('final.keys', final_key.keys)
if final_key.keys is not None:
    thisExp.addData('final.rt', final_key.rt)
thisExp.nextEntry()
routineTimer.reset()

# -- Wrap up -----------------------------------------------------------------
win.flip()
thisExp.saveAsWideText(filename + '.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()