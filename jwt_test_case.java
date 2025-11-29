package org.wso2.carbon.apimgt.impl;

import org.testng.Assert;
import org.testng.annotations.Test;

public class JWTClaimExtractorTest {

    @Test
    public void testExtractEmailClaim() {
        String payload = "{\"email\":\"user@example.com\",\"name\":\"John\"}";
        JWTClaimExtractor extractor = new JWTClaimExtractor();

        String result = extractor.getClaim(payload, "email");

        Assert.assertEquals(result, "user@example.com",
                "Email claim should be extracted correctly.");
    }
}
