using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace StocksPredictor
{
    public partial class Menu : Form
    {
        private TabControl tabControl;

        public Menu()
        {
            InitializeComponent();
            InitializeTabControl();
        }

        private void InitializeTabControl()
        {
            this.tabControl = new TabControl();

            // Create tabs
            TabPage tabPageMain = new TabPage("Main");
            TabPage tabPageSettings = new TabPage("Settings");
            TabPage tabPageThemes = new TabPage("Themes");
            TabPage tabPageAdvancedSettings = new TabPage("Advanced Settings");

            // Add tabs to TabControl
            this.tabControl.TabPages.Add(tabPageMain);
            this.tabControl.TabPages.Add(tabPageSettings);
            this.tabControl.TabPages.Add(tabPageThemes);
            this.tabControl.TabPages.Add(tabPageAdvancedSettings);

            // Set the size and location of the TabControl
            this.tabControl.Dock = DockStyle.Fill;

            // Add the TabControl to the form
            this.Controls.Add(this.tabControl);

            // Add a button to the Main tab
            Button runButton = new Button();
            runButton.Text = "Run";
            runButton.Location = new Point(10, 10);
            runButton.Click += RunButton_Click;
            tabPageMain.Controls.Add(runButton);
        }

        private void RunButton_Click(object sender, EventArgs e)
        {
            string pythonScriptPath = @"E:\Stocks Predictor GUI\Stocks_Predictor-main\main.py";
            Process.Start("python", pythonScriptPath);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
