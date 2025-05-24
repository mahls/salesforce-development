
# SOQL and SOSL Reference Guide

## Introduction

Salesforce provides two powerful query languages for searching and retrieving data from its database:

- **SOQL** (Salesforce Object Query Language) — used to retrieve records from one or more objects.
- **SOSL** (Salesforce Object Search Language) — used to perform text searches across multiple objects and fields.

---

## SOQL (Salesforce Object Query Language)

### Purpose

SOQL is similar to SQL and is used to query Salesforce records based on specific criteria.

### Basic Syntax

```sql
SELECT fieldList 
FROM objectType
WHERE condition 
ORDER BY field
LIMIT number
```

### Key Points

- Queries a single object or related objects (via relationship queries).
- Supports filtering with `WHERE`.
- Can order results with `ORDER BY`.
- Can limit number of records with `LIMIT`.

### Examples

```apex
// Get account names and phone numbers
SELECT Name, Phone FROM Account

// Get contacts with last name 'Smith'
SELECT Id, FirstName, LastName FROM Contact WHERE LastName = 'Smith'

// Get opportunities related to a specific account
SELECT Name, StageName FROM Opportunity WHERE AccountId = '001xxxxxxxxxxxx'

// Order accounts by creation date, descending
SELECT Name FROM Account ORDER BY CreatedDate DESC LIMIT 5
```

### Relationship Queries

- **Parent-to-child** (subquery):
```sql
SELECT Name, (SELECT LastName FROM Contacts) FROM Account WHERE Name LIKE 'Acme%'
```

- **Child-to-parent**:
```sql
SELECT LastName, Account.Name FROM Contact WHERE Account.Name LIKE 'Acme%'
```

---

## SOSL (Salesforce Object Search Language)

### Purpose

SOSL is optimized for performing text searches across multiple objects and fields simultaneously.

### Basic Syntax

```sql
FIND 'searchQuery' 
[RETURNING objectType(fieldList [WHERE condition])]
```

### Key Points

- Searches text, email, and phone fields.
- Can search across multiple objects in one query.
- Returns a list of lists of sObjects.

### Examples

```apex
// Search for 'Acme' in Account and Contact objects
FIND 'Acme' RETURNING Account(Id, Name), Contact(Id, FirstName, LastName)

// Search contacts where email contains 'example.com'
FIND 'example.com*' RETURNING Contact(Id, Email WHERE Email LIKE '%example.com%')
```

---

## When to Use SOQL vs SOSL

| Use Case                           | Use SOQL               | Use SOSL                     |
|----------------------------------|-----------------------|-----------------------------|
| Query records from a single object | ✅                    |                             |
| Query across multiple objects     |                       | ✅                          |
| Search by text across many fields |                       | ✅                          |
| Query with complex filters         | ✅                    |                             |
| Retrieve large volumes of records  | ✅                    |                             |

---

## Best Practices

- Use **SOQL** when you know exactly which object and fields you want.
- Use **SOSL** when you need to perform a broad text search.
- Always **limit** your results to improve performance.
- Avoid **SELECT *** queries; always specify fields.
- Use **indexed fields** in WHERE clauses to improve query performance.
- Use **relationship queries** to reduce the number of queries.

---

## Useful Resources

- [Salesforce SOQL and SOSL Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/)
- [SOQL Tutorial](https://trailhead.salesforce.com/en/content/learn/modules/apex_database/apex_database_soql)
- [SOSL Tutorial](https://trailhead.salesforce.com/en/content/learn/modules/apex_database/apex_database_sosl)

---

*Last updated: 2025-05-24*
