from pyftg.models.frame_data import FrameData
from pyftg.models.key import Key


class CommandCenter:
    def __init__(self):
        self.skill_key: list[Key] = []
        self.frame_data: FrameData = None
        self.player_number = False

    def command_call(self, str):
        if not self.skill_key:
            self.action_to_command(str)

    def action_to_command(self, str: str):
        if str == "FORWARD_WALK":
            self.create_keys("6")
        elif str == "DASH":
            self.create_keys("6 5 6")
        elif str == "BACK_STEP":
            self.create_keys("4 5 4")
        elif str == "CROUCH":
            self.create_keys("2")
        elif str == "JUMP":
            self.create_keys("8")
        elif str == "FOR_JUMP":
            self.create_keys("9")
        elif str == "BACK_JUMP":
            self.create_keys("7")
        elif str == "STAND_GUARD":
            self.create_keys("4")
        elif str == "CROUCH_GUARD":
            self.create_keys("1")
        elif str == "AIR_GUARD":
            self.create_keys("7")
        elif str == "THROW_A":
            self.create_keys("4 _ A")
        elif str == "THROW_B":
            self.create_keys("4 _ B")
        elif str == "STAND_A":
            self.create_keys("A")
        elif str == "STAND_B":
            self.create_keys("B")
        elif str == "CROUCH_A":
            self.create_keys("2 _ A")
        elif str == "CROUCH_B":
            self.create_keys("2 _ B")
        elif str == "AIR_A":
            self.create_keys("A")
        elif str == "AIR_B":
            self.create_keys("B")
        elif str == "AIR_DA":
            self.create_keys("2 _ A")
        elif str == "AIR_DB":
            self.create_keys("2 _ B")
        elif str == "STAND_FA":
            self.create_keys("6 _ A")
        elif str == "STAND_FB":
            self.create_keys("6 _ B")
        elif str == "CROUCH_FA":
            self.create_keys("3 _ A")
        elif str == "CROUCH_FB":
            self.create_keys("3 _ B")
        elif str == "AIR_FA":
            self.create_keys("9 _ A")
        elif str == "AIR_FB":
            self.create_keys("9 _ B")
        elif str == "AIR_UA":
            self.create_keys("8 _ A")
        elif str == "AIR_UB":
            self.create_keys("8 _ B")
        elif str == "STAND_D_DF_FA":
            self.create_keys("2 3 6 _ A")
        elif str == "STAND_D_DF_FB":
            self.create_keys("2 3 6 _ B")
        elif str == "STAND_F_D_DFA":
            self.create_keys("6 2 3 _ A")
        elif str == "STAND_F_D_DFB":
            self.create_keys("6 2 3 _ B")
        elif str == "STAND_D_DB_BA":
            self.create_keys("2 1 4 _ A")
        elif str == "STAND_D_DB_BB":
            self.create_keys("2 1 4 _ B")
        elif str == "AIR_D_DF_FA":
            self.create_keys("2 3 6 _ A")
        elif str == "AIR_D_DF_FB":
            self.create_keys("2 3 6 _ B")
        elif str == "AIR_F_D_DFA":
            self.create_keys("6 2 3 _ A")
        elif str == "AIR_F_D_DFB":
            self.create_keys("6 2 3 _ B")
        elif str == "AIR_D_DB_BA":
            self.create_keys("2 1 4 _ A")
        elif str == "AIR_D_DB_BB":
            self.create_keys("2 1 4 _ B")
        elif str == "STAND_D_DF_FC":
            self.create_keys("2 3 6 _ C")
        else:
            self.create_keys(str)

    def create_keys(self, str: str):
        buf = None
        commands = str.split(" ")
        if not self.frame_data.is_front(self.player_number):
            commands = self.reverse_key(commands)

        index = 0
        while index < len(commands):
            buf = Key()
            if commands[index] == "L" or commands[index] == "4":
                buf.L = True
            elif commands[index] == "R" or commands[index] == "6":
                buf.R = True
            elif commands[index] == "D" or commands[index] == "2":
                buf.D = True
            elif commands[index] == "U" or commands[index] == "8":
                buf.U = True
            elif commands[index] == "LD" or commands[index] == "1":
                buf.L = True
                buf.D = True
            elif commands[index] == "LU" or commands[index] == "7":
                buf.L = True
                buf.U = True
            elif commands[index] == "RD" or commands[index] == "3":
                buf.R = True
                buf.D = True
            elif commands[index] == "RU" or commands[index] == "9":
                buf.R = True
                buf.U = True

            if index + 2 < len(commands) and commands[index + 1] == "_":
                index += 2
            if commands[index] == "A":
                buf.A = True
            elif commands[index] == "B":
                buf.B = True
            elif commands[index] == "C":
                buf.C = True
            self.skill_key.append(buf)
            index += 1

    def set_frame_data(self, frame_data: FrameData, player_number: bool):
        self.frame_data = frame_data
        self.player_number = player_number

    def get_skill_flag(self) -> bool:
        return len(self.skill_key) > 0

    def get_skill_key(self) -> Key:
        if self.get_skill_flag():
            return self.skill_key.pop(0)
        else:
            return Key()

    def get_skill_keys(self) -> list[Key]:
        return self.skill_key

    def skill_cancel(self):
        self.skill_key.clear()

    def is_player_number(self) -> bool:
        return self.player_number

    def reverse_key(self, commands: list[str]):
        buffer = [0]*len(commands)
        for i in range(len(commands)):
            if commands[i] == "L" or commands[i] == "4":
                buffer[i] = "6"
            elif commands[i] == "R" or commands[i] == "6":
                buffer[i] = "4"
            elif commands[i] == "LD" or commands[i] == "1":
                buffer[i] = "3"
            elif commands[i] == "LU" or commands[i] == "7":
                buffer[i] = "9"
            elif commands[i] == "RD" or commands[i] == "3":
                buffer[i] = "1"
            elif commands[i] == "RU" or commands[i] == "9":
                buffer[i] = "7"
            else:
                buffer[i] = commands[i]
        return buffer
