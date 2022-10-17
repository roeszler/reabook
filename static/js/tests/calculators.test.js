const propYield = require("../calculators.js");

// Test Property Calculator
describe("Property Calculator", () => {
    describe("Property Yield Function", () => {
        test("should return 0.06 for sale price of 250,000 and 1250 pcm rent", () => {
            expect(propYield(250000, 1250)).toBe(0.06);
        })
        test("should return 0.08 for sale price of 1,875,000 and 12500 pcm rent", () => {
            expect(propYield(1875000, 12500)).toBe(0.08);
        })
    })
})
