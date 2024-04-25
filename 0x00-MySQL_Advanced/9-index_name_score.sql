-- Task 9: Create index idx_name_first_score on table names for optimizing searches by first name letter and score
CREATE INDEX idx_name_first_score ON names ( name(1), score );
