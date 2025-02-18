async function getData(url) {
    try {
        const res = await fetch(url);
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
      
        return await res.json();
    } catch (error) {
        console.log(error);
    }
  }

  async function getCategories() {
    try {
      const data = await getData("http://127.0.0.1:8000/api/v1/categories/");
      data.forEach(item => console.log(item.title_hy));
    } catch (error) {
      console.log(error);
    }
  }

  async function getProducts() {    
    try {
      const data = await getData("http://127.0.0.1:8000/api/v1/products/");
      console.log(data);
    } catch (error) {
      console.log(error);
    }
  }

  getCategories();
  getProducts();