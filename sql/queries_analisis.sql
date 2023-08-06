select provincia, fecha, p_mes from provincias as p
left join clima as c
on c.indicativo = p.indicativo
where provincia = 'Almería'

select provincia, fecha, p_mes from provincias as p
left join clima as c
on c.indicativo = p.indicativo
where provincia = 'Galicia'

select provincia, fecha, p_mes from provincias as p
left join clima as c
on c.indicativo = p.indicativo
where provincia = 'Huelva'

select provincia, fecha, p_mes from provincias as p
left join clima as c
on c.indicativo = p.indicativo
where provincia = 'A_Coruna'

select provincia, fecha, p_mes from provincias as p
left join clima as c
on c.indicativo = p.indicativo
where provincia = 'Girona'

select provincia, fecha, p_mes from provincias as p
left join clima as c
on c.indicativo = p.indicativo
where fecha like '2020%'

SELECT p.provincia, ROUND(SUM(p_mes), 2) AS total_p_mes
FROM provincias AS p
LEFT JOIN clima AS c ON c.indicativo = p.indicativo
LEFT JOIN explotaciones AS e ON p.codigo_provincia = e.codigo_provincia
WHERE fecha LIKE '2020%'
GROUP BY p.provincia;