-- Criar tabela
CREATE TABLE temperature_readings (
    id TEXT,
    "room_id/id" TEXT,
    noted_date TEXT,
    temp INT,
    "out/in" TEXT
);

-- Importar CSV automaticamente
COPY temperature_readings
FROM '/docker-entrypoint-initdb.d/IOT-temp.csv'
DELIMITER ','
CSV HEADER;

-- Views
CREATE VIEW temp_in_out AS
SELECT "out/in" AS ambiente, AVG(temp) AS avg_temp
FROM temperature_readings
GROUP BY "out/in";

CREATE VIEW leituras_por_hora AS
SELECT 
EXTRACT(HOUR FROM TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora,
COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

CREATE VIEW temp_max_min_por_dia AS
SELECT 
DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS data,
MAX(temp) AS temp_max,
MIN(temp) AS temp_min
FROM temperature_readings
GROUP BY data
ORDER BY data;

CREATE VIEW temp_in_out_timeline AS
SELECT 
TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI') AS timestamp,
"out/in" AS ambiente,
AVG(temp) AS temp
FROM temperature_readings
GROUP BY timestamp, "out/in"
ORDER BY timestamp;