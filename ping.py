exports.handler = async (event) => {
    // TODO implement
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Anz-Authentication!!! Your token is valid to AnZPlatform'),
    };
    return response;
};
