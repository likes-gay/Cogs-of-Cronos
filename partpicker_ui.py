import pytermgui as ptg
import json

class part_picker():
    def __init__(self, partID, name, desc, attack, defence, cost, part, part_manager):
        self.partID = partID
        self.name = name
        self.desc = desc
        self.attack = attack
        self.defence = defence
        self.cost = cost
        self.part = part
        self.part_manager = part_manager

    def _buy_part(self, manager):
        self.part_manager.purchase_part(self.part)
        self.window.close()
    
    def _skip_part(self, manager):
        
        self.window.close()

    def build_window(self):
        self.window = ptg.Window(
        ptg.Label(self.name.upper(), style="underline bold 167;098;060"),
        "",
        ptg.Label(f"Part Type: [52;84;79]{self.part}", style="192;139;81", parent_align=0),
        "",
        ptg.Label(f"Description: [52;84;79]{self.desc}", style="192;139;81", parent_align=0),
        "",
        ptg.Label(f"Attack: [52;84;79]{self.attack}", style="192;139;81", parent_align=0),
        "",
        ptg.Label(f"Defence: [52;84;79]{self.defence}", style="192;139;81", parent_align=0),
        "",
        ptg.Label(f"Cost: [52;84;79]{self.cost}", style="192;139;81", parent_align=0),
        "",
        ptg.Splitter(
            ptg.Button(
                "Skip",
                self._skip_part,
                width=60,
                box="DOUBLE",
            ),
            ptg.Button(
                "Buy",
                self._buy_part,
                width=60,
                box="DOUBLE",
            ),
        ),

        height=10,
        width=80,
        ).set_title("[52;84;79]Item picker").center()

        return self.window