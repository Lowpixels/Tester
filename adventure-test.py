# choose your own adventure
# Marcus Ho
# 24 September 2025

import time

def pause(t=1.2):
    time.sleep(t)

# --- Introduction / setting ---
print("You're in front of a house.")
pause(1.5)
print("The front door is open and a cold draft slips through the hallway.")
pause(1.5)
print("Your phone buzzes: 'Mr. Hale (Teacher): I'm almost there. Wait for me outside.'")
pause(1.5)

name = input("\nBefore we start, what's your name? ")
print(f"\nNice to meet you, {name}. The porch light flickers. You hear soft footsteps inside.")
pause()

# --- State variables ---
has_flashlight = False
has_note = False
trust_points = 0   # how much you trust the teacher
health = 3         # lose points on risky choices

# --- Base choice 1 ---
print("\nDo you:")
print("  A) Call out 'Hello?' into the house")
print("  B) Step inside quietly")
print("  C) Circle around to the side window")

choice1 = input("> ").strip().lower()

# Normalize quick entries
def pick(prompt, options):
    """Ask until the user types one of the allowed options (list of strings)."""
    ans = input(prompt).strip().lower()
    while ans not in options:
        ans = input(f"(Please choose {', '.join(options)}): ").strip().lower()
    return ans

#  Branch A: Call out
if choice1 == "a":
    print("\nYour voice echoes. Something shifts deeper in the hallway.")
    pause()
    print("A lamp clicks on by itself… then off. The front mat lifts slightly: there’s a tiny switch beneath it.")
    pause()

    choiceA = pick("Do you press the hidden switch (press) or leave it (leave)? ", ["press", "leave"])
    if choiceA == "press":
        print("\nA small compartment slides open in the doorframe with a FLASHLIGHT inside.")
        has_flashlight = True
        pause()
    else:
        print("\nYou decide not to touch anything. The compartment stays hidden.")
        pause()

    print("Headlights sweep across the lawn. A car stops. Mr. Hale steps out, waving.")
    pause()
    trust_points += 1

#  Branch B: Step inside
elif choice1 == "b":
    print("\nYou cross the threshold. The floorboards creak.")
    pause()
    print("On a hallway table sits a folded NOTE with your name on it.")
    pause()
    open_note = pick("Do you read the note (read) or pocket it (pocket)? ", ["read", "pocket"])
    if open_note == "read":
        print("\nThe note says: 'Do NOT let anyone in until the power is back. Basement fuse.'")
        has_note = True
        trust_points -= 1
        pause()
    else:
        print("\nYou pocket the note without reading. A draft snuffs a candle nearby.")
        pause()
    print("A door closes softly somewhere upstairs. You back to the porch as headlights approach.")
    pause()

#  Branch C: Side window
else:
    print("\nYou slip along the siding. Through the window, a stair light blinks like Morse code.")
    pause()
    decode = pick("Do you try to copy the pattern on your phone flashlight (copy) or ignore it (ignore)? ",
                  ["copy", "ignore"])
    if decode == "copy":
        print("\nYou flash the same pattern. The porch light answers once, steady.")
        has_flashlight = True
        trust_points += 1
        pause()
    else:
        print("\nYou note the weird blinking but move back to the porch, uneasy.")
        trust_points -= 1
        pause()

#  Mr. Hale arrives (nested decisions start)
print("\nMr. Hale jogs up the path, slightly out of breath.")
pause()
print('"Sorry I’m late," he says. "Did you go inside? The power’s acting strange."')
pause()

response1 = pick("Do you tell him everything (honest) or say as little as possible (vague)? ",
                 ["honest", "vague"])
if response1 == "honest":
    trust_points += 1
    if has_note:
        print('\nYou also mention the NOTE: "Don’t let anyone in until the power is back."')
        trust_points -= 1
        pause()
else:
    trust_points -= 1
    pause()

print("He tries the knob. The door opens wider with a sigh.")
pause()
enter_together = pick("Do you enter with him (enter) or ask him to wait while you check the fuse alone (fuse)? ",
                      ["enter", "fuse"])

#  Path: enter together
if enter_together == "enter":
    print("\nYou step in side by side. The hallway stretches long. A basement door stands ajar.")
    pause()
    if has_flashlight:
        print("Your flashlight cuts through the dust. Footprints lead DOWN.")
    else:
        print("It's nearly pitch black. You can just make out stairs.")
        health -= 1
    pause()

    basement_choice = pick("Go down (down) or explore the quiet upstairs first (up)? ", ["down", "up"])

    if basement_choice == "down":
        print("\nOn the fuse box, one switch is taped OFF with the same handwriting as the note.")
        pause()
        if has_note:
            print("Remembering the warning, you hesitate.")
            flip = pick("Do you flip it anyway (flip) or leave it (leave)? ", ["flip", "leave"])
        else:
            flip = pick("Flip the taped switch (flip) or leave it (leave)? ", ["flip", "leave"])

        if flip == "flip":
            print("\nThe lights blaze on. A gentle chime sounds from upstairs.")
            pause()
            if trust_points >= 1:
                print("Mr. Hale smiles. “That signal outside—good catch. You followed directions.”")
                print("A hidden panel opens revealing emergency supplies and a guest ledger.")
                print("END: **Safe House Unlocked** — you and Mr. Hale secure the house for the night.")
            else:
                print("Mr. Hale’s smile fades. “You ignored the warning, but we got lucky.”")
                print("END: **Narrow Escape** — the house is stable, but you both feel watched.")
        else:  # leave
            print("\nYou back away. The lights stay dim, but the humming stops.")
            pause()
            print("In the quiet, you find a second note: 'Trust the pattern, not the voice.'")
            print("END: **Quiet Watch** — you keep the door barred and wait for morning, unharmed.")

    else:  # upstairs first
        print("\nUpstairs, a study door is locked. A small keypad blinks 3 times, pauses, then 1 time.")
        pause()
        code = pick("Enter 31 (31) or try 13 (13)? ", ["31", "13"])
        if code == "31" and trust_points >= 1:
            print("\nClick. The study opens. Papers explain the power signals and safe-entry protocol.")
            print("Mr. Hale nods. “You read the signs.”")
            print("END: **Protocol Keeper** — you document everything and restore power safely.")
        else:
            print("\nWrong code. An alarm chirps; you both retreat.")
            print("END: **False Start** — no harm done, but the house locks itself again.")

#  Path: check fuse alone
else:
    print("\nYou ask Mr. Hale to wait on the porch while you check the basement fuse.")
    pause()
    if not has_flashlight:
        print("Without a light, you misstep on the stairs and bump your shoulder.")
        health -= 1
        pause()

    if health <= 2:
        print("You move slower now, careful of each step.")
        pause()

    print("At the fuse box, you see the taped switch and a scribbled arrow pointing to a backup generator pull-cord.")
    pause()
    solo_choice = pick("Do you pull the cord (pull) or return to ask Mr. Hale first (ask)? ", ["pull", "ask"])

    if solo_choice == "pull":
        print("\nThe generator kicks in. Lights glow warm.")
        pause()
        if has_note:
            print("The note’s warning makes sense—the generator powers the safe circuits only.")
        if trust_points <= 0:
            print("Mr. Hale looks impressed from the doorway. “You handled that.”")
        print("END: **Independent Fix** — you restore power safely and regroup with Mr. Hale.")
    else:
        print("\nYou return to the porch and share what you found.")
        pause()
        if trust_points >= 1:
            print("Together, you choose the generator over the taped fuse.")
            print("END: **Team Decision** — cautious, coordinated, and safe.")
        else:
            print("He insists on flipping the taped fuse anyway. You hesitate.")
            pause()
            print("A buzzer sounds; the house locks the fuse and reverts to generator mode automatically.")
            print("END: **Auto-Safeguard** — the house protects you from a bad call. Lesson learned.")
