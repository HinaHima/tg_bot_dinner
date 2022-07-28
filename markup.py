from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# The admin panel's buttons
btnDescription = InlineKeyboardButton (text="Изменение данных о следующем мероприятии", callback_data="btnDescription")
btnPlaces = InlineKeyboardButton (text="Изменение количества свободных мест", callback_data="btnPlaces")
btnSpam = InlineKeyboardButton (text="Рассылка", callback_data="btnSpam")
# The main menu's buttons
btnInfo = InlineKeyboardButton (text="Информация о проекте", callback_data="btnInfo")
btnNext = InlineKeyboardButton (text="Информация о следующем мероприятии", callback_data="btnNext")
btnMenu = InlineKeyboardButton (text="Возвращение в меню", callback_data="btnMenu")
btnRegister = InlineKeyboardButton (text="Запись на мероприятие", callback_data="btnRegister")
# The main menu
mainMenu = InlineKeyboardMarkup().add(btnInfo).add(btnNext)
checkRegister = InlineKeyboardMarkup().add(btnRegister)
# The admin panel
adminKB = InlineKeyboardMarkup().add(btnSpam).add(btnPlaces).add(btnDescription)