-- Customer table DDL for PostgreSQL
-- Reflects the customer data dictionary schema with validation constraints
-- Compatible with PostgreSQL 12+

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    category VARCHAR(50) NOT NULL,
    score DECIMAL(5,2) NOT NULL,
    
    -- Constraints for data validation
    CONSTRAINT chk_score_range CHECK (score >= 0.00 AND score <= 999.99),
    CONSTRAINT chk_category_values CHECK (category IN ('premium', 'standard', 'basic', 'vip')),
    CONSTRAINT chk_email_format CHECK (email IS NULL OR email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    CONSTRAINT chk_name_length CHECK (char_length(name) > 0)
);

-- Add indexes for performance
CREATE INDEX idx_customers_category ON customers(category);
CREATE INDEX idx_customers_score ON customers(score);
CREATE INDEX idx_customers_email ON customers(email) WHERE email IS NOT NULL;

-- Add comments for documentation
COMMENT ON TABLE customers IS 'Customer master data table containing core customer information';
COMMENT ON COLUMN customers.id IS 'Unique customer identifier (primary key)';
COMMENT ON COLUMN customers.name IS 'Full customer name, required field';
COMMENT ON COLUMN customers.email IS 'Customer email address, optional but must be valid format if provided';
COMMENT ON COLUMN customers.category IS 'Customer category: premium, standard, basic, or vip';
COMMENT ON COLUMN customers.score IS 'Customer score from 0.00 to 999.99';
