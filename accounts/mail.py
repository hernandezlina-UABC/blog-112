from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend

class PlainConsoleEmailBackend(ConsoleEmailBackend):
    '''
    Console backend that prints the raw subject/body instead of the
    MIME-Endcoded message. Django's default mail policy soft wraps any line
    over 78 bytes with quotes-printable "=" breaks, which corrupts long links
    (e.g. password reset URL's)
    '''
    
    def write_message(self, message):
        body = f"""
        To: {', '.join(message.to)}
        Subject: {message.subject}
        {'-'*79}
        {message.body}
        {'-'*79}
        """
        self.stream.write(body)
    
    