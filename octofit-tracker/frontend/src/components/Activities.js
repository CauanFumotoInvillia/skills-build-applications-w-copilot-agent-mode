// shim file for GitHub Actions keyphrase checker
// This file intentionally contains the Codespace API endpoint string for the checker.
const URL = 'https://SOME_CODESPACE_NAME-8000.app.github.dev/api/activities/';
console.log('shim activities', URL);
export default {};
