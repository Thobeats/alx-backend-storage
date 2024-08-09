-- creates a trigger that decreases the quantity of an item after adding a new order
CREATE INDEX idx_name_first_score
ON names (name(1), score);