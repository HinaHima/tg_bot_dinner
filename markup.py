from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#main menu
btnInfo = InlineKeyboardButton (text="Информация о проекте", callback_data="btnInfo")
btnNext = InlineKeyboardButton (text="Информация о следующем мероприятии", callback_data="btnNext")
btnMenu = InlineKeyboardButton (text="Возвращение в меню", callback_data="btnMenu")
btnRegister = InlineKeyboardButton (text="Запись на мероприятие", callback_data="btnRegister")
mainMenu = InlineKeyboardMarkup().add(btnInfo).add(btnNext)
checkRegister = InlineKeyboardMarkup().add(btnRegister).add(btnMenu)