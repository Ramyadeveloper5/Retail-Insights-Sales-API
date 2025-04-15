-- Create Table --
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    product_name TEXT NOT NULL,
    quantity INT NOT NULL,
    price NUMERIC NOT NULL
);

-- Show The Table --

SELECT * FROM sales

-- Data Insert through Table --

INSERT INTO sales(date, product_name, quantity, price) VALUES
('2025-01-01', 'Notebook A5', 15, 70.00),
('2025-01-02', 'Gel Pen', 30, 20.00),
('2025-01-03', 'Ballpoint Pen', 25, 10.00),
('2025-01-04', 'Drawing Book', 12, 100.00),
('2025-01-05', 'Eraser', 40, 5.00),
('2025-01-06', 'Sharpener', 35, 8.00),
('2025-01-07', 'Highlighter Set', 10, 150.00),
('2025-01-08', 'Stapler', 8, 170.00),
('2025-01-09', 'Whiteboard Marker', 20, 35.00),
('2025-01-10', 'Sticky Notes', 15, 35.00),
('2025-01-11', 'Sketch Pens', 20, 60.00),
('2025-01-12', 'Color Pencils', 16, 90.00),
('2025-01-13', 'Scissors', 14, 80.00),
('2025-01-14', 'Scale', 30, 20.00),
('2025-01-15', 'Glue Stick', 25, 25.00),
('2025-01-16', 'Paper Clips', 20, 30.00),
('2025-01-17', 'Paper Clips', 12, 50.00),
('2025-01-18', 'Desk Organizer', 6, 200.00),
('2025-01-19', 'File Folder', 15, 45.00),
('2025-01-20', 'Correction Tape', 18, 35.00),
('2025-01-21', 'Pencil Box', 10, 120.00),
('2025-01-22', 'Clipboard', 7, 70.00),
('2025-01-23', 'Stamp Pad', 5, 60.00),
('2025-01-24', 'Calculator', 4, 550.00),
('2025-01-25', 'Desk Calendar', 9, 150.00),
('2025-01-26', 'Desk Calendar', 10, 350.00),
('2025-01-27', 'Desk Calendar', 22, 1000.00);