from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#main menu
btnPlaces = InlineKeyboardButton (text="Изменение количества свободных мест", callback_data="btnPlaces")
btnInfo = InlineKeyboardButton (text="Информация о проекте", callback_data="btnInfo")
btnNext = InlineKeyboardButton (text="Информация о следующем мероприятии", callback_data="btnNext")
btnMenu = InlineKeyboardButton (text="Возвращение в меню", callback_data="btnMenu")
btnRegister = InlineKeyboardButton (text="Запись на мероприятие", callback_data="btnRegister")
btnSpam = InlineKeyboardButton (text="Рассылка", callback_data="btnSpam")
mainMenu = InlineKeyboardMarkup().add(btnInfo).add(btnNext)
checkRegister = InlineKeyboardMarkup().add(btnRegister)
adminKB = InlineKeyboardMarkup().add(btnSpam).add(btnPlaces)