-- Crear tabla domains
CREATE TABLE domains (
    domain_id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain TEXT NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP)
);

-- Crear tabla subdomains
CREATE TABLE subdomains (
    subdomain_id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_id INTEGER,
    subdomain TEXT NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (domain_id) REFERENCES domains (domain_id)
);

-- Crear tabla url_results
CREATE TABLE url_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subdomain_id INTEGER,
    url TEXT NOT NULL,
    status_code INTEGER,
    content TEXT,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (subdomain_id) REFERENCES subdomains (subdomain_id)
);

-- Crear tabla requests
CREATE TABLE requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    result_id INTEGER,
    url TEXT NOT NULL,
    status_code INTEGER,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (result_id) REFERENCES url_results (result_id)
);

-- Crear tabla api_keys
CREATE TABLE api_keys (
    api_key_id INTEGER PRIMARY KEY AUTOINCREMENT,
    result_id INTEGER,
    key_name TEXT,
    key_value TEXT,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (result_id) REFERENCES url_results (result_id)
);

-- Crear tabla injection_points
CREATE TABLE injection_points (
    injection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    result_id INTEGER,
    injection_type TEXT,
    injection_details TEXT,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
    FOREIGN KEY (result_id) REFERENCES url_results (result_id)
);
