import mdt as mdt
from threading import Thread


def start():
    mdt_service = Thread(target=mdt.main)
    mdt_service.start()


def run():
    mdt.status_change(True, False, False)


def exit():
    mdt.status_change(False, False, True)


def pause():
    mdt.status_change(False, True, False)


def get_cid():
    if mdt.cid_show_gui:
        return mdt.cid_show_gui
    else:
        return None


def get_cards_db(locale: str):
    if locale == "zh-CN":
        if mdt.cards_db_CN:
            return mdt.cards_db_CN
        else:
            return None
    elif locale == "zh-TW":
        if mdt.cards_db_TW:
            return mdt.cards_db_TW
        else:
            return None


def get_card_tier(cid: str):
    if mdt.ur_tier_list and mdt.sr_tier_list:
        if cid in mdt.ur_tier_list:
            return mdt.ur_tier_list[cid]["tier"]
        elif cid in mdt.sr_tier_list:
            return mdt.sr_tier_list[cid]["tier"]
        else:
            return None
    else:
        return None


def get_break_point(cid: str):
    if mdt.break_point:
        if cid in mdt.break_point:
            return mdt.break_point[cid]["tier"]
    else:
        return None
