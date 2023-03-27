using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if(checkBox1.CheckState == CheckState.Checked) //checkbox1 seleccionado
            {
                checkBox2.CheckState = CheckState.Unchecked; //checkbox2 descartado
                checkBox3.CheckState = CheckState.Unchecked; //checkbox3 descartado
                checkBox4.CheckState = CheckState.Unchecked; //checkbox4 descartado
                label5.Text = "+"; //El texto de label5 se remplazara por +
                Double res = double.Parse(textBox1.Text) + Double.Parse(textBox2.Text); // los numeros de Textbox1 y Textbox2 seran sumados
                textBox3.Text = res.ToString(); // Textbox3 mostrara el resultado
            }
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox2.CheckState == CheckState.Checked) //checkbox2 seleccionado
            {
                checkBox1.CheckState = CheckState.Unchecked; //checkbox1 descartado
                checkBox3.CheckState = CheckState.Unchecked; //checkbox3 descartado
                checkBox4.CheckState = CheckState.Unchecked; //checkbox4 descartado
                label5.Text = "-"; //El texto de label5 se remplazara por -
                Double res = double.Parse(textBox1.Text) - Double.Parse(textBox2.Text); // los numeros de Textbox1 y Textbox2 seran restados
                textBox3.Text = res.ToString(); // Textbox3 mostrara el resultado
            }

        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox3.CheckState == CheckState.Checked) //checkbox3 seleccionado
            {
                checkBox1.CheckState = CheckState.Unchecked; //checkbox1 descartado
                checkBox2.CheckState = CheckState.Unchecked; //checkbox2 descartado
                checkBox4.CheckState = CheckState.Unchecked; //checkbox4 descartado
                label5.Text = "*"; //El texto de label5 se remplazara por *
                Double res = double.Parse(textBox1.Text) * Double.Parse(textBox2.Text); //los numeros de Textbox1 y Textbox2 seran multiplicados
                textBox3.Text = res.ToString(); // Textbox3 mostrara el resultado
            }

        }

        private void checkBox4_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox4.CheckState == CheckState.Checked) //checkbox4 seleccionado
            {
                checkBox1.CheckState = CheckState.Unchecked; //checkbox1 descartado
                checkBox2.CheckState = CheckState.Unchecked; //checkbox2 descartado
                checkBox3.CheckState = CheckState.Unchecked; //checkbox3 descartado
                label5.Text = ":"; //El texto de label5 se remplazara por :
                Double res = double.Parse(textBox1.Text) / Double.Parse(textBox2.Text); //los numeros de Textbox1 y Textbox2 seran divididos
                textBox3.Text = res.ToString(); // Textbox3 mostrara el resultado
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Clear(); //Limpiar textbox1
            textBox2.Clear(); //Limpiar textbox2
            textBox3.Clear(); //Limpiar textbox3
            checkBox1.CheckState = CheckState.Unchecked; //checkbox1 descartado
            checkBox2.CheckState = CheckState.Unchecked; //checkbox2 descartado
            checkBox3.CheckState = CheckState.Unchecked; //checkbox3 descartado
            checkBox4.CheckState = CheckState.Unchecked; //checkbox4 descartado
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit(); //Salir de la Aplicacion
        }

        private void label8_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            validar();
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            validar();
        }

        public void validar()
        {
            if(textBox1.Text != "" & textBox2.Text != "")
            {
                checkBox1.Enabled = true; //checkBox1 Activado
                checkBox2.Enabled = true; //checkBox2 Activado
                checkBox3.Enabled = true; //checkBox3 Activado
                checkBox4.Enabled = true; //checkBox4 Activado
            }
            else
            {
                checkBox1.Enabled = false; //checkBox1 Desactivado
                checkBox2.Enabled = false; //checkBox2 Desactivado
                checkBox3.Enabled = false; //checkBox3 Desactivado
                checkBox4.Enabled = false; //checkBox4 Desactivado
            }

        }
    }
}
