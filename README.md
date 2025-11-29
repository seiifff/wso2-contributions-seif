# wso2-contributions-seif
Evidence of my WSO2 Community Program contributions, including documentation fixes, test cases, a bug fix, and a technical blog post. Total points: 5.
 
Author: Seif Ferooz  
Total Points: 5 

Each item follows the guidelines and corresponds to the official point structure.

---

## 1. Documentation Fix (1 Point)

**File:** `documentation_fix.md`  
Improved the Throttling documentation for WSO2 API Manager by clarifying the relationship between API-level and application-level throttling policies, including examples and corrected explanations.

---

## 2. Missing Test Case (1 Point)

**File:** `jwt_test_case.java`  
Added a missing unit test for the `JWTClaimExtractor` class to ensure correct extraction of string-based JWT claims such as `email`.  
This improves coverage and prevents regression in authentication-related functionality.

---

## 3. Blog Post About a WSO2 Product (1 Point)

**File:** `blog_post.md`  
Wrote a complete article titled **"Building a Modern API Ecosystem with WSO2 API Manager"** explaining API governance challenges and how WSO2 API Manager solves them.  
Includes a real-world case study implementing API-M in an online bookstore project.

(DOCX version also available.)

---

## 4. Bug Fix Contribution (2 Points)

**File:** `label_checker.py`  
Identified and resolved a reliability issue in the `label_checker` workflow used in the WSO2 API Manager repository.  
The original script crashed if GitHub issue headings were missing.  
The fix introduces safer parsing, fallback logic, and prevents workflow failures.

---

## Total Points: 5

These contributions meet and exceed the 3-point minimum requirement for the WSO2 Community Program.
