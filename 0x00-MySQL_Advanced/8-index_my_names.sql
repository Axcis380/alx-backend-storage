--Task 8: Create an index named "idx_name_first" on the table "names" for optimizing simple searches based on the first letter of the name
CREATE INDEX idx_name_first ON names ( name(1) );
