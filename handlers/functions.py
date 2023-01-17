

def status_users(message_id):
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                 (message_id,))
    user_status = cursor.fetchone()
    if user_status[0] == 'Rab':
        user_status2 = '<b>♦️Владелец</b>'

    if user_status[0] == 'Admin':
        user_status2 = '<b>👮ADMIN</b>'

    if user_status[0] == 'Player':
        user_status2 = '<b>💤Игрок</b>'
    if user_status[0] == 'vip':
        user_status2 = '<b>⭐️VIP</b>'
    if user_status[0] == 'premium':
        user_status2 = '<b>💎PREMIUM</b>'
    if user_status[0] == 'delux':
        user_status2 = '<b>🔥DELUXE</b>'
    return user_status2





