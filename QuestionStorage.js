// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {
  getFirestore,
  collection,
  addDoc,
  getDoc, // For reading a single document
  getDocs, // For reading multiple documents
  updateDoc, // For updating a document
  deleteDoc, // For deleting a document
  doc // For referencing a specific document
} from "firebase/firestore";

// Your web app's Firebase configuration
// This information is typically found in your Firebase project settings
const firebaseConfig = {
  apiKey: "AIzaSyCdlgAxAt2PhAF26jbazr1yoDUD_V-wkmU",
  authDomain: "infinite-socrates.firebaseapp.com",
  projectId: "infinite-socrates",
  storageBucket: "infinite-socrates.firebasestorage.app",
  messagingSenderId: "677068126117",
  appId: "1:677068126117:web:20a6774a4bb047deac5a4c",
  measurementId: "G-VN1SYSZN60"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(app);

// --- C (Create) ---
async function addQuestion(questionData) {
  try {
    const docRef = await addDoc(collection(db, "questions"), questionData);
    console.log("Question created with ID: ", docRef.id);
    return docRef.id; // Return the ID of the newly created document
  } catch (e) {
    console.error("Error adding document: ", e);
    throw e; // Re-throw for error handling in calling code
  }
}

// --- R (Read) ---

// Read a single question by its ID
async function getQuestionById(questionId) {
  try {
    const questionRef = doc(db, "questions", questionId);
    const questionSnap = await getDoc(questionRef);

    if (questionSnap.exists()) {
      console.log("Question data:", questionSnap.data());
      return { id: questionSnap.id, ...questionSnap.data() };
    } else {
      console.log("No such question!");
      return null;
    }
  } catch (e) {
    console.error("Error getting document:", e);
    throw e;
  }
}

// Read all questions from the collection
async function getAllQuestions() {
  try {
    const questionsCol = collection(db, "questions");
    const questionSnapshot = await getDocs(questionsCol);
    const questionList = questionSnapshot.docs.map(doc => ({
      id: doc.id,
      ...doc.data()
    }));
    console.log("All questions:", questionList);
    return questionList;
  } catch (e) {
    console.error("Error getting all documents:", e);
    throw e;
  }
}

// --- U (Update) ---
async function updateQuestion(questionId, updatedFields) {
  try {
    const questionRef = doc(db, "questions", questionId);
    await updateDoc(questionRef, updatedFields);
    console.log("Question with ID", questionId, "updated successfully.");
  } catch (e) {
    console.error("Error updating document:", e);
    throw e;
  }
}

// --- D (Delete) ---
async function deleteQuestion(questionId) {
  try {
    await deleteDoc(doc(db, "questions", questionId));
    console.log("Question with ID", questionId, "deleted successfully.");
  } catch (e) {
    console.error("Error deleting document:", e);
    throw e;
  }
}

// --- Example Usage ---
async function demonstrateCrud() {
  // 1. Create a new question
  console.log("\n--- Creating a new question ---");
  const newQuestionData = {
    text: "What is the perimeter of a square with side length 5?",
    equation: "P = 4s, s=5",
    conceptId: "geometry-perimeter",
    difficulty: 1,
    guidanceSteps: [
      "What is the definition of perimeter?",
      "How many sides does a square have?",
      "Are the sides of a square equal in length?"
    ],
    answer: "20",
    points: 5,
    tags: ["geometry", "perimeter"]
  };
  let newQuestionId;
  try {
    newQuestionId = await addQuestion(newQuestionData);
  } catch (error) {
    console.error("Failed to create question:", error);
    return; // Stop if creation fails
  }


  // 2. Read the newly created question
  console.log(`\n--- Reading question with ID: ${newQuestionId} ---`);
  const fetchedQuestion = await getQuestionById(newQuestionId);


  // 3. Update the question
  console.log(`\n--- Updating question with ID: ${newQuestionId} ---`);
  await updateQuestion(newQuestionId, { difficulty: 2, points: 7 });
  await getQuestionById(newQuestionId); // Read again to see the update


  // 4. Read all questions
  console.log("\n--- Reading all questions ---");
  await getAllQuestions();


  // 5. Delete the question
  console.log(`\n--- Deleting question with ID: ${newQuestionId} ---`);
  await deleteQuestion(newQuestionId);
  await getQuestionById(newQuestionId); // Try to read after deletion
}

// Call the demonstration function
demonstrateCrud();
