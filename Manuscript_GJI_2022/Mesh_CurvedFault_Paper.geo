//+
Point(1) = {-700, 0, 0, 5.0};
//+
Point(2) = {400, 0, 0, 5.0};
//+
Point(3) = {400, -500, 0, 25.0};
//+
Point(4) = {-700, -500, 0, 25.0};
//+
Point(5) = {0, 0, 0, 5.0};
//+
Point(6) = {-90, -60, 0, 5.0};
//+
Point(7) = {-37.5, -15, 0, 5.0};
//+
Point(8) = {-69, -37.5, 0, 5.0};
//+
Point(9) = {-450, -500, 0, 25.0};
//+
Line(1) = {1, 4};
//+
Line(2) = {4, 9};
//+
Line(3) = {9, 3};
//+
Line(4) = {3, 2};
//+
Line(5) = {2, 5};
//+
Line(6) = {5, 1};
//+
Spline(7) = {5, 7, 8, 6};
//+
Spline(8) = {6, 9};
//+
Line Loop(1) = {6, 1, 2, -8, -7};
//+
Plane Surface(1) = {1};
//+
Line Loop(2) = {5, 7, 8, 3, 4};
//+
Plane Surface(2) = {2};
//+
Physical Line("top", 1) = {6, 5};
//+
Physical Line("left", 2) = {1};
//+
Physical Line("bottom", 3) = {2, 3};
//+
Physical Line("right", 4) = {4};
//+
Physical Line("fault", 5) = {7};
//+
Physical Line("extended fault", 6) = {8};
//+
Physical Surface("blockleft", 7) = {1};
//+
Physical Surface("blockright", 8) = {2};
