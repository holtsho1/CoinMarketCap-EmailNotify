def SendGmailFunc():
    import smtplib, ssl

    port = 465  # For SSL
    password = 'Cpurple93!'

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("coinmarketcapnotify@gmail.com", password)
        # create different variables for sending email
        sender_email = "coinmarketcapnotify@gmail.com"
        receiver_email = "coinmarketcapnotify@gmail.com"
        message = """\
        Subject: New Crypto
    
        There is a new crypto on coinmarketcap."""

        # Send email here
        server.sendmail(sender_email, receiver_email, message)
        return print('email sent')


