// Acutis_Codes/Javascript/Data_Fundamentals/Variables_%26_DataTypes/datatypes.js

/**
 * Javascript Data Types
 * 
 */


var name = "Paul";
const nameConst = "Joseph";
let nameLet = "Joseph";

// Lists
var students = ["Paul", "Joseph", "John", "Peter"];
const studentConst = ["Paul", "Joseph", "John", "Peter"];
let studentsLet = ["Paul", "Joseph", "John", "Peter"];

// Dictionaries
const courses = {
    1: ["Web Designing", "Discrete Math", "Data Structures"],
    2: ["Advanced Web Designing", "Python", "Java"],
    3: ["IOTs", "Advanced IOTs", "Advanced Data Structures"],
    4: ["Research", "Machine Learning", "Artificial Intelligence"]
};

// Trees

class TreeNode {
    constructor(value) {
        this.value = value;
        this.children = [];
    }

    addChild(childNode) {
        this.children.push(childNode);
    }
}

class Tree {
    constructor(rootValue) {
        this.root = new TreeNode(rootValue);
    }
}

// Example: building a course tree like your dictionary example
const tree = new Tree("Courses");

const year1 = new TreeNode("Year 1");
const year2 = new TreeNode("Year 2");

year1.addChild(new TreeNode("Web Designing"));
year1.addChild(new TreeNode("Discrete Math"));
year1.addChild(new TreeNode("Data Structures"));

year2.addChild(new TreeNode("Advanced Web Designing"));
year2.addChild(new TreeNode("Python"));
year2.addChild(new TreeNode("Java"));

tree.root.addChild(year1);
tree.root.addChild(year2);

console.log(JSON.stringify(tree, null, 2));

console.log(courses[1][0]); // Web Designing