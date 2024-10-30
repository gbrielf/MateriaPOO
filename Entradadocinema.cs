class Entradadocinema{
    public int dia{get;set;}
    public int hora{get;set;}

    public Entradadocinema(int d, int h)
    {
        public dia = d;
        public hora = h;
    }

    public float Valordaentrada()
    {   string[] nasemana = {'segunda', 'terça', 'quinta', };
        string[] fimdesemana = {'sexta', 'sabado', 'domingo'};
        
        if (dia != 'quarta')
        {
            if (hora >= 17 || hora <= 24)
            {
                if (nasemana.Contains(dia))
                {
                    return 24;
                }
                else if(fimdesemana.Contais(dia))
                {
                    return 30;
                }
            }
            else
            {
                if(nasemana.Contains(dia))
                {
                    return 16;
                }
                else if(fimdesemana.Contais(dia))
                {
                    return 20;
                }
            }
        }
        else
        {
            return 8;
        }
    }

}