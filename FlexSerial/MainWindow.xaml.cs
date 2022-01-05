using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.IO.Ports;
using System.Text.RegularExpressions;

namespace FlexSerial
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        SerialPort serialPort;
        public MainWindow()
        {
            InitializeComponent();

            serialPort = new SerialPort();
            serialPort.DataReceived += SerialPort_DataReceived;

            start.IsEnabled = !serialPort.IsOpen;
            pause.IsEnabled = serialPort.IsOpen;

            List<String> coms = SerialPort.GetPortNames().OrderBy(o => Int32.Parse(o.Split('M')[1])).ToList();

            foreach (String comName in coms)
            {
                comNames.Items.Add(comName);
            }
            comNames.SelectedIndex = 0;
        }

        private void SerialPort_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            Dispatcher.Invoke(() =>
           {
               text.Text += serialPort.ReadExisting();
               text.SelectionStart = text.Text.Length;
               text.ScrollToEnd();
           });

        }

        private void start_Click(object sender, RoutedEventArgs e)
        {
            serialPort.PortName = comNames.SelectedItem.ToString();
            serialPort.BaudRate = 9600;
            try
            {
                serialPort.Open();
                info.Text = "Port opened successfully";
            }
            catch (Exception ex)
            {
                info.Text = ex.Message;
            }

            start.IsEnabled = !serialPort.IsOpen;
            pause.IsEnabled = serialPort.IsOpen;
        }
        void baud_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = new Regex("[^0-9]+").IsMatch(e.Text);
        }

        private void pause_Click(object sender, RoutedEventArgs e)
        {
            serialPort.Close();
            start.IsEnabled = !serialPort.IsOpen;
            pause.IsEnabled = serialPort.IsOpen;
        }

        private void cls_Click(object sender, RoutedEventArgs e)
        {
            text.Text = "";
        }
    }
}
