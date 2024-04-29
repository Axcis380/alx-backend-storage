-- Task 8: Create index idx_name_first on table names for optimizing searches by first name letter
CREATE INDEX idx_name_first ON names ( name(1) );
