// Acutis_Codes/C%2B%2B/Data_Fundamentals/Variables_%26_DataTypes/datatypes.c%2B%2B
// Data Types in C++

// Acutis_Codes/Cpp/Data_Fundamentals/Variables_And_DataTypes/variables.cpp
// This file explains variables and data types in C++.
/*
Variables are containers for storing data values.
Data types define the kind of value a variable can hold.

Let's explore some common data types in C++:
*/

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <any>
#include <optional>

using namespace std;

int main() {
    // String: Represents a sequence of characters.
    string name = "John Doe";

    // Integer: Represents a whole number.
    int age = 25;

    // Double: Represents a floating-point number.
    double height = 5.9;

    // Boolean: Represents a true or false value.
    bool isStudent = true;

    // Vector (List): Represents an ordered collection of values.
    vector<string> hobbies = {"Reading", "Traveling", "Coding"};

    // Map: Represents a collection of key-value pairs.
    map<string, int> scores = {
        {"Math", 90},
        {"Science", 85},
        {"English", 88}
    };

    // Set: Represents an unordered collection of unique values.
    set<string> uniqueColors = {"Red", "Green", "Blue"};

    // Any: Represents a variable that can hold any data type (C++17).
    any variable = string("I can be anything!");

    // Optional: Represents a value that may or may not be present (nullable, C++17).
    optional<string> nullableString = nullopt;

    // auto: type is inferred from the assigned value, like Dart's 'var'.
    auto inferredString = string("This is a string");
    auto inferredInt = 42;
    auto inferredDouble = 3.14;
    auto inferredBool = true;

    // Const: set once, cannot be reassigned (like Dart's 'final').
    const string finalName = "Jane Doe";

    // Constexpr: compile-time constant, cannot be changed (like Dart's 'const').
    constexpr double pi = 3.14159;

    // Print everything to verify
    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "Height: " << height << endl;
    cout << "Is Student: " << (isStudent ? "true" : "false") << endl;

    cout << "Hobbies: [";
    for (size_t i = 0; i < hobbies.size(); ++i) {
        cout << hobbies[i];
        if (i != hobbies.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    cout << "Scores: {";
    size_t count = 0;
    for (const auto& pair : scores) {
        cout << pair.first << ": " << pair.second;
        if (++count != scores.size()) cout << ", ";
    }
    cout << "}" << endl;

    cout << "Unique Colors: {";
    count = 0;
    for (const auto& color : uniqueColors) {
        cout << color;
        if (++count != uniqueColors.size()) cout << ", ";
    }
    cout << "}" << endl;

    cout << "Any variable: " << any_cast<string>(variable) << endl;
    cout << "Nullable String: " << (nullableString.has_value() ? nullableString.value() : "null") << endl;
    cout << "Inferred String: " << inferredString << endl;
    cout << "Inferred Int: " << inferredInt << endl;
    cout << "Inferred Double: " << inferredDouble << endl;
    cout << "Inferred Bool: " << (inferredBool ? "true" : "false") << endl;
    cout << "Final Name: " << finalName << endl;
    cout << "Pi: " << pi << endl;

    return 0;
}