from enum import Enum

from pyftg.models.enums.int_action import IntAction


class Action(Enum):
    NEUTRAL = "neutral"
    STAND = "stand"
    FORWARD_WALK = "forward_walk"
    DASH = "dash"
    BACK_STEP = "back_step"
    CROUCH = "crouch"
    JUMP = "jump"
    FOR_JUMP = "for_jump"
    BACK_JUMP = "back_jump"
    AIR = "air"
    STAND_GUARD = "stand_guard"
    CROUCH_GUARD = "crouch_guard"
    AIR_GUARD = "air_guard"
    STAND_GUARD_RECOV = "stand_guard_recov"
    CROUCH_GUARD_RECOV = "crouch_guard_recov"
    AIR_GUARD_RECOV = "air_guard_recov"
    STAND_RECOV = "stand_recov"
    CROUCH_RECOV = "crouch_recov"
    AIR_RECOV = "air_recov"
    CHANGE_DOWN = "change_down"
    DOWN = "down"
    RISE = "rise"
    LANDING = "landing"
    THROW_A = "throw_a"
    THROW_B = "throw_b"
    THROW_HIT = "throw_hit"
    THROW_SUFFER = "throw_suffer"
    STAND_A = "stand_a"
    STAND_B = "stand_b"
    CROUCH_A = "crouch_a"
    CROUCH_B = "crouch_b"
    AIR_A = "air_a"
    AIR_B = "air_b"
    AIR_DA = "air_da"
    AIR_DB = "air_db"
    STAND_FA = "stand_fa"
    STAND_FB = "stand_fb"
    CROUCH_FA = "crouch_fa"
    CROUCH_FB = "crouch_fb"
    AIR_FA = "air_fa"
    AIR_FB = "air_fb"
    AIR_UA = "air_ua"
    AIR_UB = "air_ub"
    STAND_D_DF_FA = "stand_d_df_fa"
    STAND_D_DF_FB = "stand_d_df_fb"
    STAND_F_D_DFA = "stand_f_d_dfa"
    STAND_F_D_DFB = "stand_f_d_dfb"
    STAND_D_DB_BA = "stand_d_db_ba"
    STAND_D_DB_BB = "stand_d_db_bb"
    AIR_D_DF_FA = "air_d_df_fa"
    AIR_D_DF_FB = "air_d_df_fb"
    AIR_F_D_DFA = "air_f_d_dfa"
    AIR_F_D_DFB = "air_f_d_dfb"
    AIR_D_DB_BA = "air_d_db_ba"
    AIR_D_DB_BB = "air_d_db_bb"
    STAND_D_DF_FC = "stand_d_df_fc"

    def to_int(self) -> int:
        return IntAction[self.name].value

    @classmethod
    def from_int(cls, action: int):
        return Action[IntAction(action).name]
