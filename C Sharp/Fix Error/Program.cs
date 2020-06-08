using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Исправить_ошибку
{
    class Program
    {
        static void Main(string[] args)
        {
            ProcessStartInfo psi = new ProcessStartInfo();
            //Имя запускаемого приложения
            psi.FileName = "cmd";
            //команда, которую надо выполнить
            psi.Arguments = @"/k pip install requests bs4 img2pdf natsort pyperclip";
            //  /c - после выполнения команды консоль закроется
            //  /к - не закрывать консоль после выполнения команды
            Process.Start(psi);
        }
    }
}
