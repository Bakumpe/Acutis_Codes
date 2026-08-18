// Acutis_Codes/Dart/Data_Fundamentals/Variables_%26_DataTypes/variables.dart
// This file explains variables and data types in Dart programming language.
/*
Variables are containers for storing data values.
Data types define the kind of value a variable can hold.

Let's explore some common data types in Dart:
*/

void main() {
  // String: Represents a sequence of characters.
  String name = "John Doe";

  // Integer: Represents a whole number.
  int age = 25;

  // Double: Represents a floating-point number.
  double height = 5.9;

  // Boolean: Represents a true or false value.
  bool isStudent = true;

  // List: Represents an ordered collection of values.
  List<String> hobbies = ["Reading", "Traveling", "Coding"];

  // Map: Represents a collection of key-value pairs.
  Map<String, int> scores = {
    "Math": 90,
    "Science": 85,
    "English": 88
  };

  // Set: Represents an unordered collection of unique values.
  Set<String> uniqueColors = {"Red", "Green", "Blue"};

  // Dynamic: Represents a variable that can hold any data type.
  dynamic variable = "I can be anything!";

  // Null: Represents the absence of a value.
  String? nullableString = null;

  // var: type is inferred from the assigned value.
  var inferredString = "This is a string"; // Inferred as String
  var inferredInt = 42; // Inferred as int
  var inferredDouble = 3.14; // Inferred as double
  var inferredBool = true; // Inferred as bool

  // Final: can only be set once, cannot be reassigned.
  final String finalName = "Jane Doe";

  // Const: compile-time constant, cannot be changed.
  const double pi = 3.14159;

  // Print everything to verify
  print("Name: $name");
  print("Age: $age");
  print("Height: $height");
  print("Is Student: $isStudent");
  print("Hobbies: $hobbies");
  print("Scores: $scores");
  print("Unique Colors: $uniqueColors");
  print("Dynamic variable: $variable");
  print("Nullable String: $nullableString");
  print("Inferred String: $inferredString");
  print("Inferred Int: $inferredInt");
  print("Inferred Double: $inferredDouble");
  print("Inferred Bool: $inferredBool");
  print("Final Name: $finalName");
  print("Pi: $pi");
}