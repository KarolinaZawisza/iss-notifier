import smtplib

def send_notification(is_night, iss_position):
    if is_night and iss_position:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user='example@email.com', password='password')
            connection.sendmail(
                from_addr='example@email.com',
                to_addrs='email@example.com',
                msg='SUBJECT:ISS has arrived!\n\n'
                    'The ISS is currently above your position!\n'
                    'Go outside and try to find it!'
            )
        print('Email send!')
    else:
        print('ISS currently isn\'t anywhere near you!')
