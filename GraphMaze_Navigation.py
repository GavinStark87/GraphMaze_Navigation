#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Graph Maze Navigation Task
MenoMaps Project - UC Irvine Spatial Neuroscience Lab
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

# Create data directory before anything tries to write logs
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

# -- Background colors (PsychoPy rgb -1 to 1 scale) -------------------------
COLOR_BLACK = [0, 0, 0]
COLOR_BLUE  = [0.2, 0.55, 0.95]     # lighter blue -- path distance trials
COLOR_PEACH = [0.914, 0.506, 0.090] # peach        -- straight-line trials

# -- Question text map -------------------------------------------------------
question_map = {
    'route': 'Which is the shortest path distance from the start?',
    'line':  'Which is the shortest straight-line distance from the start?'
}

# -- Instruction slide text -------------------------------------------------
SLIDE1_TITLE = 'Practice Trials + Instructions'

SLIDE1_BODY = (
    "You are going to be shown a series of objects from one of two environments "
    "you've previously learned in this study (one from the first session, one from today).\n\n"
    "You will be given an object that you should imagine you have been placed in front of "
    "(at the top of the screen), and then indicate, of two possible options, which object is "
    "closest to the starting object, either via shortest path distance "
    "(if you were to wayfind via set paths) or shortest straight-line distance "
    "(if you could walk in a straight line to it).\n\n"
    "If you think the object on the left is closest, you'll press the left button. "
    "Similarly, if you think the object on the right is closest, you'll press the right button.\n\n"
    "First, we'll practice with an example environment."
)

SLIDE2_BODY = (
    "You will now begin the task. There will be a total of 40 trials across 2 different "
    "environments that you have learned (one from your first session, one from today's session). "
    "You will have 10 seconds to respond to each trial, and you will not be given feedback "
    "on your performance.\n\n"
    "As a final reminder, you will be asked to indicate which object is closer to your "
    "starting point either via shortest path distance or shortest straight-line distance "
    "(they may not be the same answer!).\n\n"
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

# Practice maze display
maze_image = visual.ImageStim(
    win=win, name='maze_image',
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.03), size=(0.75, 0.75),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
maze_title_stim = visual.TextStim(win=win, name='maze_title_stim',
    text='Example Practice Maze', font='Arial',
    pos=(0, 0.43), height=0.048, wrapWidth=1.4, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=-1.0)

# Environment maze image
env_maze_image = visual.ImageStim(
    win=win, name='env_maze_image',
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.06), size=(0.72, 0.72),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Environment label
envClock = core.Clock()
env_label = visual.TextStim(win=win, name='env_label',
    text='', font='Arial',
    pos=(0, 0.43), height=0.048, wrapWidth=1.4, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=0.0)
# FIX 1: pos y moved from -0.43 to -0.46 so the prompt sits lower on maze screens
env_advance = visual.TextStim(win=win, name='env_advance',
    text='Press any number to continue.',
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

# Feedback -- left side
fb_text_left = visual.TextStim(win=win, name='fb_text_left',
    text='', font='Arial',
    pos=(-0.65, 0.02), height=0.046, wrapWidth=0.25, ori=0,
    color=[0, 0.32, 0], colorSpace='rgb', opacity=1, depth=0.0)
fb_line_left = visual.Line(win=win, name='fb_line_left',
    start=(-0.52, -0.07), end=(-0.35, -0.17),
    lineWidth=3.0, lineColor=[0, 0.32, 0], lineColorSpace='rgb')
fb_head_left = visual.ShapeStim(win=win, name='fb_head_left',
    vertices=[(-0.35, -0.17), (-0.395, -0.167), (-0.375, -0.133)],
    fillColor=[0, 0.32, 0], lineColor=[0, 0.32, 0],
    lineColorSpace='rgb', fillColorSpace='rgb', opacity=1, depth=-1.0)

# Feedback -- right side
fb_text_right = visual.TextStim(win=win, name='fb_text_right',
    text='', font='Arial',
    pos=(0.65, 0.02), height=0.046, wrapWidth=0.25, ori=0,
    color=[0, 0.32, 0], colorSpace='rgb', opacity=1, depth=0.0)
fb_line_right = visual.Line(win=win, name='fb_line_right',
    start=(0.52, -0.07), end=(0.35, -0.17),
    lineWidth=3.0, lineColor=[0, 0.32, 0], lineColorSpace='rgb')
fb_head_right = visual.ShapeStim(win=win, name='fb_head_right',
    vertices=[(0.35, -0.17), (0.375, -0.133), (0.395, -0.167)],
    fillColor=[0, 0.32, 0], lineColor=[0, 0.32, 0],
    lineColorSpace='rgb', fillColorSpace='rgb', opacity=1, depth=-1.0)

# End screen
endClock = core.Clock()
thankyou = visual.TextStim(win=win, name='thankyou',
    text='You have now completed the experiment.\n\nThank you for your participation!',
    font='Arial', pos=(0, 0.1), height=0.06, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=0.0)
finalslide = visual.TextStim(win=win, name='finalslide',
    text='Press any number to exit.',
    font='Arial', pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=-1.0)
final_key = keyboard.Keyboard()

# ===========================================================================
# HELPER FUNCTIONS
# ===========================================================================

def load_conditions(csv_path):
    """
    Load a conditions CSV. Quits with a clear console message if the file
    is not found or if importConditions raises any exception.
    FIX 2: removed thisExp.abort() from the error path -- it can itself
    throw if called before all data is set up, causing a confusing double
    crash. win.close() + core.quit() is sufficient.
    """
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


def show_text_slide(title_text, body_text):
    """
    Display a text-only instruction slide on a black background.
    Advances on any number key. No PNG file required.
    When title_text is provided, also shows colour-coded distance hints.
    """
    win.color = COLOR_BLACK
    slideClock = core.Clock()
    vis_comps = []

    if title_text:
        title_stim = visual.TextStim(win,
            text=title_text, font='Arial',
            pos=(0, 0.39), height=0.060,
            wrapWidth=1.5, color='white', colorSpace='rgb',
            bold=True, depth=0.0)
        vis_comps.append(title_stim)
        body_pos_y = 0.03
    else:
        body_pos_y = 0.12

    body_stim = visual.TextStim(win,
        text=body_text, font='Arial',
        pos=(0, body_pos_y), height=0.036,
        wrapWidth=1.5, color='white', colorSpace='rgb',
        depth=-1.0)
    vis_comps.append(body_stim)

    if title_text:
        path_hint = visual.TextStim(win,
            text='Blue background  =  path distance trials',
            font='Arial', pos=(0, -0.40), height=0.032,
            color=COLOR_BLUE, colorSpace='rgb', depth=-2.0)
        line_hint = visual.TextStim(win,
            text='Peach background  =  straight-line distance trials',
            font='Arial', pos=(0, -0.44), height=0.032,
            color=COLOR_PEACH, colorSpace='rgb', depth=-3.0)
        vis_comps.extend([path_hint, line_hint])

    advance_stim = visual.TextStim(win,
        text='Press any number to continue.',
        font='Arial', pos=(0, -0.47), height=0.031,
        color=[0.4, 0.4, 0.4], colorSpace='rgb', depth=-4.0)
    vis_comps.append(advance_stim)

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
            theseKeys = slide_resp.getKeys(
                keyList=['1','2','3','4','5','6','7','8','9','0'],
                waitRelease=False)
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


def show_practice_maze():
    """
    Show the fruit practice maze image with title and advance prompt.
    Number keys to advance.
    FIX 1: env_advance is now included so the 'press any number' prompt
    appears on this screen too, at the lowered y=-0.46 position.
    """
    win.color = COLOR_BLACK
    maze_image.setImage('stimuli/prac_maze.png')
    maze_resp = keyboard.Keyboard()
    # FIX 1: add env_advance to the component list
    display_comps = [maze_image, maze_title_stim, env_advance]
    for comp in display_comps:
        comp.status = NOT_STARTED
        comp.tStart = None
    maze_resp.status = NOT_STARTED
    maze_resp.keys = []
    _allKeys = []
    continueRoutine = True
    mazeClock = core.Clock()
    _timeToFirstFrame = win.getFutureFlipTime(clock='now')
    mazeClock.reset(-_timeToFirstFrame)
    frameN = -1
    while continueRoutine:
        tThisFlip = win.getFutureFlipTime(clock=mazeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        for comp in display_comps:
            if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                comp.frameNStart = frameN
                comp.tStart = mazeClock.getTime()
                comp.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(comp, 'tStartRefresh')
                comp.setAutoDraw(True)
        waitOnFlip = False
        if maze_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            maze_resp.frameNStart = frameN
            maze_resp.tStart = mazeClock.getTime()
            maze_resp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(maze_resp, 'tStartRefresh')
            maze_resp.status = STARTED
            waitOnFlip = True
            win.callOnFlip(maze_resp.clock.reset)
            win.callOnFlip(maze_resp.clearEvents, eventType='keyboard')
        if maze_resp.status == STARTED and not waitOnFlip:
            theseKeys = maze_resp.getKeys(
                keyList=['1','2','3','4','5','6','7','8','9','0'],
                waitRelease=False)
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


def show_env_label(label_text, maze_path=None):
    """
    Display environment label on black background. Number keys to advance.
    If maze_path is provided, shows the maze image below the label.
    """
    win.color = COLOR_BLACK
    env_label.setText(label_text)

    display_comps = [env_label, env_advance]
    if maze_path:
        env_maze_image.setImage(maze_path)
        display_comps = [env_label, env_maze_image, env_advance]

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
            theseKeys = env_resp.getKeys(
                keyList=['1','2','3','4','5','6','7','8','9','0'],
                waitRelease=False)
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


def run_trial(trialData, practice=False):
    """
    Run one trial. Returns (keys, rt, corr).
    practice=True shows green feedback arrow after response.
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

    # Countdown timer -- trial ends automatically after 10 seconds
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
            theseKeys = trial_resp.getKeys(
                keyList=['1', '2'], waitRelease=False)
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

        # End trial if 10 seconds have elapsed with no response
        if trialCountdown.getTime() <= 0:
            continueRoutine = False

        if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
            core.quit()
        if continueRoutine:
            win.flip()

    for comp in vis_comps:
        comp.setAutoDraw(False)

    # Handle no-response case
    if trial_resp.keys in ['', [], None]:
        trial_resp.keys = None
        trial_resp.rt   = None
        trial_resp.corr = 0

    # -- Practice feedback ---------------------------------------------------
    if practice:
        corr_label = str(trialData['corrLabel'])
        corr_side  = str(trialData['corrAns'])

        if corr_side == 'left':
            fb_text_left.setText('Correct answer:\n' + corr_label)
            fb_comps = [fb_text_left, fb_line_left, fb_head_left]
        else:
            fb_text_right.setText('Correct answer:\n' + corr_label)
            fb_comps = [fb_text_right, fb_line_right, fb_head_right]

        for comp in vis_comps:
            comp.setAutoDraw(True)
        for comp in fb_comps:
            comp.status = NOT_STARTED
            comp.tStart = None

        fbClock = core.Clock()
        routineTimer.reset()
        routineTimer.add(2.0)
        _timeToFirstFrame = win.getFutureFlipTime(clock='now')
        fbClock.reset(-_timeToFirstFrame)
        frameN = -1
        while routineTimer.getTime() > 0:
            tThisFlip = win.getFutureFlipTime(clock=fbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            for comp in fb_comps:
                if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                    comp.frameNStart = frameN
                    comp.tStart = fbClock.getTime()
                    comp.tStartRefresh = tThisFlipGlobal
                    win.timeOnFlip(comp, 'tStartRefresh')
                    comp.setAutoDraw(True)
            if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
                core.quit()
            win.flip()
        for comp in vis_comps + fb_comps:
            comp.setAutoDraw(False)
        routineTimer.reset()

    win.color = COLOR_BLACK
    return trial_resp.keys, trial_resp.rt, trial_resp.corr


# ===========================================================================
# EXPERIMENT FLOW
# ===========================================================================

# 1. Instruction text slide
show_text_slide(SLIDE1_TITLE, SLIDE1_BODY)

# 2. Practice maze -- first showing
show_practice_maze()

# 3. Fruit practice block (4 trials, sequential)
fruit_handler = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=load_conditions('nav_task_practice_fruit.csv'),
    seed=None, name='fruit_practice')
thisExp.addLoop(fruit_handler)

trial_count = 0
for thisFruit in fruit_handler:
    currentLoop = fruit_handler
    if thisFruit is not None:
        for paramName in thisFruit:
            exec('{} = thisFruit[paramName]'.format(paramName))

    if trial_count == 2:
        show_practice_maze()

    show_fixation(1.0)
    respKeys, respRT, respCorr = run_trial(thisFruit, practice=True)

    fruit_handler.addData('trial_resp.keys', respKeys)
    fruit_handler.addData('trial_resp.corr', respCorr)
    if respKeys is not None:
        fruit_handler.addData('trial_resp.rt', respRT)
    fruit_handler.addData('trial_type', thisFruit['trial_type'])
    fruit_handler.addData('cue_image.file', thisFruit['cueImage'])

    trial_count += 1
    routineTimer.reset()
    thisExp.nextEntry()

# 4. Pre-task instruction slide
show_text_slide('', SLIDE2_BODY)

# ---------------------------------------------------------------------------
# BRICK block: practice THEN main trials
# ---------------------------------------------------------------------------

# 5. Brick maze env label + practice
show_env_label('Environment: brick maze', maze_path='stimuli/brick_maze.png')

brick_prac_handler = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=load_conditions('nav_task_practice_brick.csv'),
    seed=None, name='brick_practice')
thisExp.addLoop(brick_prac_handler)

for thisBrick in brick_prac_handler:
    currentLoop = brick_prac_handler
    if thisBrick is not None:
        for paramName in thisBrick:
            exec('{} = thisBrick[paramName]'.format(paramName))

    show_fixation(1.0)
    respKeys, respRT, respCorr = run_trial(thisBrick, practice=True)

    brick_prac_handler.addData('trial_resp.keys', respKeys)
    brick_prac_handler.addData('trial_resp.corr', respCorr)
    if respKeys is not None:
        brick_prac_handler.addData('trial_resp.rt', respRT)
    brick_prac_handler.addData('trial_type', thisBrick['trial_type'])
    brick_prac_handler.addData('cue_image.file', thisBrick['cueImage'])

    routineTimer.reset()
    thisExp.nextEntry()

# FIX 2: flush all stale key presses before entering the main trial loop.
# A number key held or released at the end of the last practice trial can
# be picked up immediately by the first main trial, ending it before any
# stimulus has drawn -- most likely cause of the post-practice crash.
event.clearEvents()
defaultKeyboard.clearEvents()

# 6. Brick maze main trials (randomised, no feedback)
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
    respKeys, respRT, respCorr = run_trial(thisTrial, practice=False)

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

# ---------------------------------------------------------------------------
# HEDGE block: practice THEN main trials
# ---------------------------------------------------------------------------

# 7. Hedge maze env label + practice
show_env_label('Environment: hedge maze', maze_path='stimuli/hedge_maze.png')

hedge_prac_handler = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=load_conditions('nav_task_practice_hedge.csv'),
    seed=None, name='hedge_practice')
thisExp.addLoop(hedge_prac_handler)

for thisHedge in hedge_prac_handler:
    currentLoop = hedge_prac_handler
    if thisHedge is not None:
        for paramName in thisHedge:
            exec('{} = thisHedge[paramName]'.format(paramName))

    show_fixation(1.0)
    respKeys, respRT, respCorr = run_trial(thisHedge, practice=True)

    hedge_prac_handler.addData('trial_resp.keys', respKeys)
    hedge_prac_handler.addData('trial_resp.corr', respCorr)
    if respKeys is not None:
        hedge_prac_handler.addData('trial_resp.rt', respRT)
    hedge_prac_handler.addData('trial_type', thisHedge['trial_type'])
    hedge_prac_handler.addData('cue_image.file', thisHedge['cueImage'])

    routineTimer.reset()
    thisExp.nextEntry()

# FIX 2 (same as brick): flush stale key presses before hedge main trials
event.clearEvents()
defaultKeyboard.clearEvents()

# 8. Hedge maze main trials (randomised, no feedback)
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
    respKeys, respRT, respCorr = run_trial(thisTrial, practice=False)

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
# END ROUTINE
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
        theseKeys = final_key.getKeys(
            keyList=['1','2','3','4','5','6','7','8','9','0'],
            waitRelease=False)
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