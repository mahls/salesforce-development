
# Salesforce Front-End Code Examples

A comprehensive collection of common Salesforce front-end code snippets including Lightning Web Components (LWC) and Aura components.

---

## Lightning Web Components (LWC) Examples

### 1. Basic Hello World
```javascript
// helloWorld.js
import { LightningElement } from 'lwc';
export default class HelloWorld extends LightningElement {
    message = 'Hello, Salesforce!';
}
```
```html
<!-- helloWorld.html -->
<template>
    <p>{message}</p>
</template>
```

---

### 2. Public Property with @api
```javascript
import { LightningElement, api } from 'lwc';
export default class ChildComponent extends LightningElement {
    @api recordId;
}
```

---

### 3. Handling Events and Dispatching Custom Events
```javascript
// childComponent.js
this.dispatchEvent(new CustomEvent('myevent', { detail: { data: 'some data' } }));
```
```javascript
// parentComponent.js
handleMyEvent(event) {
    console.log('Received:', event.detail.data);
}
```

---

### 4. Wire Service to Call Apex Method
```javascript
import { LightningElement, wire } from 'lwc';
import getAccounts from '@salesforce/apex/AccountController.getAccounts';

export default class AccountList extends LightningElement {
    @wire(getAccounts) accounts;
}
```

---

### 5. Imperative Apex Call
```javascript
import { LightningElement } from 'lwc';
import getAccounts from '@salesforce/apex/AccountController.getAccounts';

export default class AccountImperative extends LightningElement {
    accounts;
    error;

    connectedCallback() {
        getAccounts()
            .then(result => {
                this.accounts = result;
            })
            .catch(error => {
                this.error = error;
            });
    }
}
```

---

### 6. Template Conditional Rendering
```html
<template if:true={isVisible}>
    <p>Visible content here</p>
</template>
```

### 7. Looping Over Data
```html
<template for:each={accounts.data} for:item="account">
    <p key={account.Id}>{account.Name}</p>
</template>
```

---

### 8. Two-way Data Binding with Input
```html
<template>
    <lightning-input label="Name" value={name} onchange={handleChange}></lightning-input>
    <p>You typed: {name}</p>
</template>
```
```javascript
import { LightningElement, track } from 'lwc';
export default class InputExample extends LightningElement {
    @track name = '';

    handleChange(event) {
        this.name = event.target.value;
    }
}
```

---

### 9. Styling Components (CSS)
```css
/* helloWorld.css */
p {
    color: blue;
    font-weight: bold;
}
```

---

### 10. Using Lightning Data Service (LDS) to load Record
```javascript
import { LightningElement, wire, api } from 'lwc';
import { getRecord } from 'lightning/uiRecordApi';

const FIELDS = ['Account.Name', 'Account.Phone'];

export default class AccountRecord extends LightningElement {
    @api recordId;
    @wire(getRecord, { recordId: '$recordId', fields: FIELDS })
    account;
}
```

---

## Aura Components Examples

### 1. Basic Aura Component
```html
<aura:component>
    <aura:attribute name="message" type="String" default="Hello Aura!"/>
    <p>{!v.message}</p>
</aura:component>
```

---

### 2. Aura Component Controller Method
```javascript
({
    doInit : function(component, event, helper) {
        var action = component.get("c.getAccounts");
        action.setCallback(this, function(response) {
            var state = response.getState();
            if(state === "SUCCESS") {
                component.set("v.accounts", response.getReturnValue());
            }
        });
        $A.enqueueAction(action);
    }
})
```

---

### 3. Aura Component with Event Handling
```html
<aura:component>
    <aura:handler name="init" value="{!this}" action="{!c.doInit}"/>
    <aura:attribute name="accounts" type="Account[]"/>
    <aura:iteration items="{!v.accounts}" var="acc">
        <p>{!acc.Name}</p>
    </aura:iteration>
</aura:component>
```

---

### 4. Lightning App Builder Usage
> Drag and drop LWC or Aura components onto pages with the Lightning App Builder UI tool.

---

### Notes:
- **LWC is the recommended modern front-end framework** for Salesforce development.
- Aura components are still supported for legacy and advanced use cases.
- Use **Lightning Data Service** wherever possible to reduce Apex calls.
- Styling should be scoped and use CSS modules per component.

---

*Last updated: 2025-05-24*
