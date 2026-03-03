-- Esquema extraído como código diretamente do banco de dados, não deve ser executado de uma vez para evitar comportamentos
-- estranhos; algumas tabelas e relações assumem que outras já existem, portanto é recomendada a criação manual do banco
-- a partir desse esquema

CREATE TABLE public.escolas (
  id integer NOT NULL DEFAULT nextval('escolas_id_seq'::regclass),
  escola text NOT NULL,
  sigla text UNIQUE,
  fund integer NOT NULL,
  CONSTRAINT escolas_pkey PRIMARY KEY (id)
);
CREATE TABLE public.quesitos (
  id integer NOT NULL DEFAULT nextval('quesitos_id_seq'::regclass),
  quesito text NOT NULL UNIQUE,
  sigla text NOT NULL UNIQUE,
  CONSTRAINT quesitos_pkey PRIMARY KEY (id)
);
CREATE TABLE public.resultados (
  escola integer,
  ano integer NOT NULL,
  quesito integer,
  jurado text NOT NULL,
  nota real,
  CONSTRAINT resultados_escola_fkey FOREIGN KEY (escola) REFERENCES public.escolas(id),
  CONSTRAINT resultados_quesito_fkey FOREIGN KEY (quesito) REFERENCES public.quesitos(id)
);