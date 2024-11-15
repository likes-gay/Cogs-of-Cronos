import pytermgui as ptg

def create_park_picker_window(label, description, attack, defence, cost, type):
    return ptg.Window(
        ptg.Label(label.upper(), style="underline bold 167;098;060"),
        "",
        ptg.Label(f"Part Type: [52;84;79]{type}", style="192;139;81", parent_align=0),
        "",
        ptg.Label(f"Description: [52;84;79]{description}", style="192;139;81", parent_align=0),
        "",
        ptg.Label(f"Attack: [52;84;79]{attack}", style="192;139;81", parent_align=0),
        "",
        ptg.Label(f"Defence: [52;84;79]{defence}", style="192;139;81", parent_align=0),
        "",
        ptg.Label(f"Cost: [52;84;79]{cost}", style="192;139;81", parent_align=0),
        "",
        ptg.Button(
            "Submit",
            lambda *_: submit(manager, window),
            width=60,
            box="DOUBLE",
        ),
        height=10,
        width=80,
    ).set_title("[52;84;79]Item picker").center()

with ptg.WindowManager() as manager:
    window = create_park_picker_window("Retractable Claw Legs", "Sharp mechanised claws that can enter / retract for swift slashing attacks and enhanced grip on surfaces", 8, 3, 5, "Legs")
    manager.add(window)