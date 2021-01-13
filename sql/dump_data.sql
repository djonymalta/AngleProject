--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: clock_clockapi; Type: TABLE; Schema: public; Owner: djonymalta
--

CREATE TABLE public.clock_clockapi (
    id uuid NOT NULL,
    hours integer NOT NULL,
    minuts integer NOT NULL,
    angle double precision NOT NULL,
    date timestamp with time zone NOT NULL
);


ALTER TABLE public.clock_clockapi OWNER TO djonymalta;

--
-- Data for Name: clock_clockapi; Type: TABLE DATA; Schema: public; Owner: djonymalta
--

COPY public.clock_clockapi (id, hours, minuts, angle, date) FROM stdin;
6e4d8d05-18e7-4bb8-bb09-09b9f076b951	3	0	90	2021-01-12 21:00:00-03
fd8af5ea-ff36-46cb-95f2-9dd3dea0ae08	6	0	180	2021-01-12 21:00:00-03
56678847-36f3-4aa1-9f63-e65ac622060a	9	0	90	2021-01-12 21:00:00-03
145259c6-b995-4908-90c1-5cc2571fafce	1	30	135	2021-01-12 21:00:00-03
\.


--
-- Name: clock_clockapi clock_clockapi_pkey; Type: CONSTRAINT; Schema: public; Owner: djonymalta
--

ALTER TABLE ONLY public.clock_clockapi
    ADD CONSTRAINT clock_clockapi_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

