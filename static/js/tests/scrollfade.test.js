let scroll = require("../scrollfade");

describe('Selected', () => {
    describe("Check class has changed Function", () => {
        test("expects class content to change to 'selected'", () => {
            buttonClick();
            expect(document.getElementsByClassName("time-slot").innerHTML).toEqual("selected");
        })
    });

    describe("Check class Function", () => {
        test("expects class content to not be 'selected' by default", () => {
            expect(document.getElementsByClassName("time-slot").innerHTML).toNotEqual("selected");
        })
    });
})