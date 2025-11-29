# Documentation Improvement: Throttling Behavior in WSO2 API Manager

## Issue
The existing throttling documentation does not clearly explain how subscription throttling and application throttling interact, which often leads to incorrect configurations.

## Improvement
This update adds a clarified explanation and an example to demonstrate which throttling tier takes precedence.

## Updated Explanation
WSO2 API Manager evaluates throttling in the following order:

1. API-Level Subscription Tier  
2. API Resource Throttling  
3. Application-Level Throttling  
4. Advanced Throttling Policies  

The lowest limit always wins.

## Example
- API Tier: Silver → 100 req/min  
- Application Tier: Gold → 500 req/min  

**Effective limit: 100 req/min**

## Example Snippet
```xml
<ThrottlePolicy>
  <PolicyType>API</PolicyType>
  <Tier>Silver</Tier>
  <Limit>
    <RequestsPerMinute>100</RequestsPerMinute>
  </Limit>
</ThrottlePolicy>
```

## Value
This clarification helps developers avoid misconfigurations and ensures predictable throttling behavior.
