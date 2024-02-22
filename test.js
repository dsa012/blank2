const sendEmail = async ({ message, email }) => {
    try {
      const response = await fetch(
        `https://mrlectus-stackup-6cd355c4b177.herokuapp.com/send`,
        {
          method: "POST",
          body: JSON.stringify({ message, email }),
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
  
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
  
      const contentType = response.headers.get("content-type");
      if (!contentType || !contentType.includes("application/json")) {
        throw new TypeError("The response does not contain valid JSON");
      }
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Error sending email:", error);
      // Handle the error as needed, e.g., return a custom error response
      return { error: "Failed to send email" };
    }
  };
  
  
sendEmail({ message: "test", email: "cekol90858@gexige.com" })
    .then((response) => {
        console.log(response); // handle the response as needed
    })
    .catch((error) => {
        console.error(error); // handle any errors
    });
