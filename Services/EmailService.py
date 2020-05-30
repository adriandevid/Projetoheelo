
import smtplib
import configparser
from email.message import EmailMessage

class EmailService:
    def __init__(self, ToEmail, CodeVerific):
        self.ToEmail = ToEmail
        self.CodeVerific = CodeVerific
        self.Config = configparser.RawConfigParser()
        self.Config.read('C:/Users/PC/Documents/ProjetoHeelo/Settings/Email.conf')
    def CreateEmailFormater(self):
        msg = EmailMessage()
        msg['Subject'] = "Envio de email"
        msg['From'] = self.Config.get("Email", "EMAIL_ADDRESS")
        msg['To'] = self.ToEmail

        msg.set_content('This is a plain text email')
        msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
        <head>
            <title></title>
        </head>
        <body>
        <div marginwidth="0" marginheight="0" style="background-color:#f1f1f1;min-width:600px;padding:0">
        
            <table style="background-color:#f1f1f1;min-width:600px" width="100%" bgcolor="#f1f1f1">
                <tbody><tr>
                <td style="min-width:600px" width="100%" valign="top" align="center">
                <center>
        
                <table style="min-width:600px" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#f1f1f1">
                    <tbody><tr>
                    <td align="center">
                    <table style="min-width:600px" width="100%" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                        <tr height="50">
                            <td style="line-height:1px;font-size:1px" width="100%" height="50">&nbsp;</td>
                        </tr>
                        <tr>
                            <td align="center">
                                <table style="min-width:600px" cellspacing="0" cellpadding="0" border="0">
                                    <tbody>
                                        <tr>
                                            <td valign="middle" align="center">
                                                <div style="max-height:50px">
                                                    <!-- Esta div armazena a logo -->
                                                    <div>
                                                        <a><img alt="Instituto Federal de Sergipe" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Instituto_Federal_de_Sergipe_-_Marca_Vertical_2015.svg/274px-Instituto_Federal_de_Sergipe_-_Marca_Vertical_2015.svg.png" style="width:110px; height:auto; margin:0px " title="IFS">
                                                        </a>
                                                    </div>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    <table style="min-width:600px" width="100%" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                        <tr>
                            <td align="center">
                            <table style="min-width:600px" width="600" cellspacing="0" cellpadding="0" border="0">
                            <tbody><tr height="50">
                            <td style="line-height:1px;font-size:1px" width="100%" height="50">&nbsp;</td>
                        </tr>
                        <tr>
                            <td style="font-family:arial,helvetica,sans-serif;font-size:24px;color:#313131;text-align:center;line-height:75px" align="left">
                                <!-- Esta div armazena a string "Nome do aplicativo - Email de Verificação" -->
                                <div style="font-family:arial,helvetica,sans-serif;font-size:24px;color:#313131;text-align:center;line-height:50px">
                                    Nome do aplicativo - Email de Verificação
                                </div>
        
                            </td>
                        </tr>
                        <tr height="0">
                        <td style="line-height:1px;font-size:1px" width="100%" height="30">&nbsp;</td>
                        </tr>
                        </tbody>
                    </table>
                    </td>
                    </tr>
                    </tbody>
                </table>
                </td>
                </tr>
                </tbody>
            </table>
        
        
            <table style="min-width:600px" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#f1f1f1">
                <tbody><tr>
                <td align="center">
                <table style="min-width:600px;background-color:#ffffff" width="600" cellspacing="0" cellpadding="0" border="0" bgcolor="#ffffff">
                    <tbody><tr>
                    <td align="center">
                    <table style="min-width:400px" width="400" cellspacing="0" cellpadding="0" border="0">
                        <tbody>
                            <tr height="30">
                                <td style="line-height:1px;font-size:1px" width="100%" height="30">&nbsp;</td>
                            </tr>
                        <tr>
                            <td style="font-family:arial,helvetica,sans-serif;font-size:16px;color:#313131;line-height:24px" align="left">
                                <div style="font-family:arial,helvetica,sans-serif;	font-size:16px;	color:#313131;	line-height:24px">
                                Bem-vindo ao aplicativo "Nome do aplicativo",<br><br>
                                Verifique seu endereço de e-mail usando o código abaixo para concluir a configuração da conta!
                                <br><br>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td style="font-family:arial,helvetica,sans-serif;color:#313131;text-align:center;font-size:50px;letter-spacing:5px;line-height:120px" align="center">
                                <div style="font-family:arial,helvetica,sans-serif;color:#313131;text-align:center;font-size:50px;letter-spacing:5px;line-height:120px">
                                {CodeVerific}
                                </div>
                            </td>
                        </tr>
                        <tr height="30">
                            <td style="line-height:1px;font-size:1px" width="100%" height="30">&nbsp;</td>
                        </tr>
                        <tr>
                            <td style="font-family:arial,helvetica,sans-serif;font-size:16px;color:#313131;line-height:24px" align="left">
                                <div style="font-family:arial,helvetica,sans-serif;font-size:16px;color:#313131;line-height:24px">
                                Seu código de verificação expirará em 30 minutos, portanto, use-o o mais rápido possível.
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td style="font-family:arial,helvetica,sans-serif;font-size:16px;color:#313131;line-height:24px" align="left">
                                <div style="font-family:arial,helvetica,sans-serif;font-size:16px;color:#313131;line-height:24px">
                                    <br><br>
                                Obrigado,<br>"Nome do time de desenvolvedores"<br><br>
                                </div>
                            </td>
                        </tr>
                        <tr height="50">
                        <td style="line-height:1px;font-size:1px" width="100%" height="30">&nbsp;</td>
                        </tr>
                        </tbody>
                    </table>
                    </td>
                    </tr>
                    </tbody>
                </table>
                </td>
                </tr>
                </tbody>
            </table>
        
            <table style="min-width:600px" width="100%" cellspacing="0" cellpadding="0" border="0">
            <tbody><tr>
            <td align="center">
            <table style="min-width:600px" width="600" cellspacing="0" cellpadding="0" border="0">
            <tbody><tr height="15">
            <td style="line-height:1px;font-size:1px" width="100%" height="20">&nbsp;</td>
            </tr>
            <tr>
            <td align="center">
            <table style="min-width:560px" width="560" cellspacing="0" cellpadding="0" border="0">
            <tbody><tr>
            <td align="center">
            <div style="font-family:arial,helvetica,sans-serif;font-weight:bold;font-size:14px;color:#313131;text-align:center;line-height:26px">
            <a style="text-decoration:none;color:#6bae7c" href="https://link.epicgames.com/click/5ebca1d4bdf12e31020a6fae/aHR0cHM6Ly9oZWxwLmVwaWNnYW1lcy5jb20/5ebca1d47e553f157d12695eB7e89becf" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://link.epicgames.com/click/5ebca1d4bdf12e31020a6fae/aHR0cHM6Ly9oZWxwLmVwaWNnYW1lcy5jb20/5ebca1d47e553f157d12695eB7e89becf&amp;source=gmail&amp;ust=1590804206215000&amp;usg=AFQjCNHL54iibEIWWPayFSTzSQSn9xGstA">ajuda.nomedoaplicativo.com.br</a><br>
            </div>
            </td>
            </tr>
            <tr height="20">
            <td style="line-height:1px;font-size:1px" width="100%" height="20">&nbsp;</td>
            </tr>
            <tr>
            <td align="center">
            <div style="font-family:arial,helvetica,sans-serif;font-size:12px;color:#858585;text-align:center;line-height:20px">
            <p>© 2020 Nome do Aplicativo, Todos os direitos reservados. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut porta venenatis massa, quis porttitor quam feugiat id. Quisque orci leo, ultricies viverra pellentesque vel, tempus at ipsum. Nulla non diam viverra, ultrices mauris sed, accumsan tellus. Sed in tempus risus, luctus venenatis enim.</p>
            <!--<p>© 2004-2020 Epic Games, Inc. All rights reserved. Epic, Epic Games, Epic Games Store, the Epic Games logo, Unreal, Unreal Engine 4, UE4, the Unreal Engine logo, Fortnite, and Fortnite (stylized) are trademarks or registered trademarks of Epic Games, Inc. in the United States of America and elsewhere. Other brands and product names are the trademarks of their respective owners.</p>-->
            <br>
            <a href="https://link.epicgames.com/click/5ebca1d4bdf12e31020a6fae/aHR0cHM6Ly93d3cuZXBpY2dhbWVzLmNvbS90b3M/5ebca1d47e553f157d12695eB6c51aca2" style="color:#0aaff1" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://link.epicgames.com/click/5ebca1d4bdf12e31020a6fae/aHR0cHM6Ly93d3cuZXBpY2dhbWVzLmNvbS90b3M/5ebca1d47e553f157d12695eB6c51aca2&amp;source=gmail&amp;ust=1590804206215000&amp;usg=AFQjCNFeIbzUUlgnDBzomgpzcgr3GFQ9Jw">Termos de Serviço</a> | <a href="https://link.epicgames.com/click/5ebca1d4bdf12e31020a6fae/aHR0cHM6Ly93d3cuZXBpY2dhbWVzLmNvbS9wcml2YWN5cG9saWN5/5ebca1d47e553f157d12695eB2e57cb9b" style="color:#0aaff1" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://link.epicgames.com/click/5ebca1d4bdf12e31020a6fae/aHR0cHM6Ly93d3cuZXBpY2dhbWVzLmNvbS9wcml2YWN5cG9saWN5/5ebca1d47e553f157d12695eB2e57cb9b&amp;source=gmail&amp;ust=1590804206215000&amp;usg=AFQjCNF5pZ5QHhXx5CTzbx0OsoADk_VRCQ">Política de Privacidade</a>
            </div>
            </td>
            </tr>
            <tr height="20">
            <td style="line-height:1px;font-size:1px" width="100%" height="20">&nbsp;</td>
            </tr>
            <tr height="20">
            <td style="font-family:arial,helvetica,sans-serif;font-size:12px;color:#858585;text-align:center;line-height:20px" width="100%"></td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            </td>
            </tr>
            </tbody>
            </table>
            </center>
            </td>
            </tr>
            </tbody>
            </table>
        </div>
        </body>
        </html>
        """.format(CodeVerific=self.CodeVerific), subtype='html')
        return msg
    def send_email(self, subject, msg):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com:465')
            server.login(str(self.Config.get("Email", "EMAIL_ADDRESS")), str(self.Config.get("Email", "PASSWORD")))
            server.send_message(msg)
            server.quit()
            print("Success: Email sent!")
        except Exception as inst:
            print(inst)

#send = EmailService('mezessantos36@gmail.com', 1234456)
#prep = send.CreateEmailFormater()
#send.send_email(prep['Subject'], prep)
