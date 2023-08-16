#!/bin/python3
import uinput
import pygame
import enum 

#TOP PANEL
IC0A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},    #polarity 1 means button is actuated when signal high, polarity 0, is button is actuated when signal is low
                        1: {"polarity": 1, "key": uinput.KEY_0},    #some buttons require a specific polarity setting to actuate when pressed as opposed to actuate when released
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#TOP PANEL
IC0B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 0, "key": uinput.KEY_0},
                        5: {"polarity": 0, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_0},
                        7: {"polarity": 0, "key": uinput.KEY_0}
                    }  
#TOP PANEL
IC1A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#TOP PANEL
IC1B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 0, "key": uinput.KEY_0},
                        5: {"polarity": 0, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_0},
                        7: {"polarity": 0, "key": uinput.KEY_0}
                    }
#TOP PANEL
IC2A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#TOP PANEL
IC2B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 0, "key": uinput.KEY_0},
                        5: {"polarity": 0, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_0},
                        7: {"polarity": 0, "key": uinput.KEY_0}
                    }  
#FRONT SIDE PANEL
IC3A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#FRONT SIDE PANEL
IC3B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }  
#FRONT SIDE PANEL
IC4A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#FRONT SIDE PANEL
IC4B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#BACK SIDE PANEL
IC5A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 0, "key": uinput.KEY_0},
                        4: {"polarity": 0, "key": uinput.KEY_0},
                        5: {"polarity": 0, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#BACK SIDE PANEL
IC5B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 0, "key": uinput.KEY_0},
                        7: {"polarity": 0, "key": uinput.KEY_0}
                    }
#BACK SIDE PANEL
IC6A_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }
#BACK SIDE PANEL
IC6B_uinput_map =   {     
                        0: {"polarity": 1, "key": uinput.KEY_0},
                        1: {"polarity": 1, "key": uinput.KEY_0},
                        2: {"polarity": 1, "key": uinput.KEY_0},
                        3: {"polarity": 1, "key": uinput.KEY_0},
                        4: {"polarity": 1, "key": uinput.KEY_0},
                        5: {"polarity": 1, "key": uinput.KEY_0},
                        6: {"polarity": 1, "key": uinput.KEY_0},
                        7: {"polarity": 1, "key": uinput.KEY_0}
                    }

#create dictionary to hold uinput mappings
button_uinput_map = {   
			            '0A':IC0A_uinput_map,
                        '0B':IC0B_uinput_map,
                        '1A':IC1A_uinput_map, 
                        '1B':IC1B_uinput_map,
                        '2A':IC2A_uinput_map,
                        '2B':IC2B_uinput_map,
                        '3A':IC3A_uinput_map,
                        '3B':IC3B_uinput_map,
                        '4A':IC4A_uinput_map,
                        '4B':IC4B_uinput_map,
                        '5A':IC5A_uinput_map,
                        '5B':IC5B_uinput_map,
                        '6A':IC6A_uinput_map,
                        '6B':IC6B_uinput_map,
                    }


#Key to sound maps

IC0A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC0B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC1A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/autotargetOff.wav",
                            1: "./sounds/autotargetOn.wav"
                        },
                        7:{
                            0: "./sounds/toepowerOff.wav",
                            1: "./sounds/toepowerOn.wav"
                        }
                    }  

IC1B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC2A_sound_map = {     
			            0: { #Port's Position Number
                            0: "",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "",
                            1: "./sounds/toes.wav"
                        },
                        2:{
                            0: "./sounds/veganfart.mp3",
                            1: "./sounds/atootieOn.wav"
                        },
                        3:{
                            0: "./sounds/wetfart.mp3",
                            1: "./sounds/buttcrack.wav"
                        },
                        4:{
                            0: "",
                            1: "./sounds/driedpee.wav"
                        },
                        5:{
                            0: "./sounds/chargefart.mp3",
                            1: "./sounds/poop.wav"
                        },
                        6:{
                            0: "",
                            1: "./sounds/footface.wav"
                        },
                        7:{
                            0: "",
                            1: "./sounds/dabadu.wav"
                        }
                    }  

IC2B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC3A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC3B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC4A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC4B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC5A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC5B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/reactor1Off.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/reactor1On.wav"   #"On" state
                        },
                        1: {
                            0: "",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC6A_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

IC6B_sound_map = {     
			            0: { #Port's Position Number
                            0: "./sounds/startupsequence.wav",  #"Off" state, note some buttons have negative polarity and off is on!  
                            1: "./sounds/startupsequence.wav"   #"On" state
                        },
                        1: {
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        2:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        3:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        4:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        5:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        6:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        },
                        7:{
                            0: "./sounds/startupsequence.wav",
                            1: "./sounds/startupsequence.wav"
                        }
                    }  

#create dictionary to hold sound mappings
button_sound_map = {   
			            '0A':IC0A_sound_map,
                        '0B':IC0B_sound_map,
                        '1A':IC1A_sound_map, 
                        '1B':IC1B_sound_map,
                        '2A':IC2A_sound_map,
                        '2B':IC2B_sound_map,
                        '3A':IC3A_sound_map,
                        '3B':IC3B_sound_map,
                        '4A':IC4A_sound_map,
                        '4B':IC4B_sound_map,
                        '5A':IC5A_sound_map,
                        '5B':IC5B_sound_map,
                        '6A':IC6A_sound_map,
                        '6B':IC6B_sound_map,
                    }










#enumeration definitions for each panel and button name in the spaceship
class TopPanel_IC0_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 
class TopPanel_IC0_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 

class TopPanel_IC1_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 
class TopPanel_IC1_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2 

class TopPanel_IC2_A(enum.Enum):
    A0_IC2_Launch2=0 
    A1_IC2_Toes=1
    A2_IC2_Atootie=2
    A3_IC2_ButtCrack=3
    A4_IC2_DriedPee=4
    A5_IC2_Poop=5
    A6_IC2_FootFace=6
    A7_IC2_Dabadu=7
class TopPanel_IC2_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2     

class FrontSidePanel_IC3_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   
class FrontSidePanel_IC3_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   

class FrontSidePanel_IC4_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   
class FrontSidePanel_IC4_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   


class BackSidePanel_IC5_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   
class BackSidePanel_IC5_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   

class BackSidePanel_IC6_A(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   
class BackSidePanel_IC6_B(enum.Enum):
    A0_IC5_LifeSupport=1 
    A1_IC5_PowerBank=2   


#create dictionary to hold IO expander button definitions,  this is how the buttons are physically configured in the spaceship
button_definitions = {  '0A':TopPanel_IC0_A,
                        'TOPPANEL_IC0_PORTA':TopPanel_IC0_A,
                        '0B':TopPanel_IC0_B,
                        'TOPPANEL_IC0_PORTB':TopPanel_IC0_B,
                        '1A':TopPanel_IC1_A,
                        'TOPPANEL_IC1_PORTA':TopPanel_IC1_A,
                        '1B':TopPanel_IC1_B,
                        'TOPPANEL_IC1_PORTB':TopPanel_IC1_B,
                        '2A':TopPanel_IC2_A,
                        'TOPPANEL_IC2_PORTA':TopPanel_IC2_A,
                        '2B':TopPanel_IC2_B,
                        'TOPPANEL_IC2_PORTB':TopPanel_IC2_B,

                        '3A':FrontSidePanel_IC3_A,
                        'FRONTSIDEPANEL_IC3_PORTA':FrontSidePanel_IC3_A,
                        '3B':FrontSidePanel_IC3_B,
                        'FRONTSIDEPANEL_IC3_PORTB':FrontSidePanel_IC3_B,
                        '4A':FrontSidePanel_IC4_A,
                        'FRONTSIDEPANEL_IC4_PORTA':FrontSidePanel_IC4_A,
                        '4B':FrontSidePanel_IC4_B,
                        'FRONTSIDEPANEL_IC4_PORTB':FrontSidePanel_IC4_B,

                        '5A':BackSidePanel_IC5_A,
                        'BACKSIDEPANEL_IC5_PORTA':BackSidePanel_IC5_A,
                        '5B':BackSidePanel_IC5_B,
                        'BACKSIDEPANEL_IC5_PORTB':BackSidePanel_IC5_B,
                        '6A':BackSidePanel_IC6_A,
                        'BACKSIDEPANEL_IC6_PORTA':BackSidePanel_IC6_A,
                        '6B':BackSidePanel_IC6_B,
                        'BACKSIDEPANEL_IC6_PORTB':BackSidePanel_IC6_B
                        }

                      