using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{

    int mode = 0;
    ArrayList material;
    
    void Start()
    {
        material = new ArrayList();

    }
    IEnumerator TestCoroutine()
    {
        for (int z = 0; z < 11; z++)
        {
            for (int y = -5; y < 6; y++)
            {
                for (int x = -5; x < 6; x++)
                {
                    GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
                    cube.transform.position = new Vector3(x, y, z);
                    cube.GetComponent<Renderer>().material.color = new Color(Random.Range(0.0f, 1.0f), Random.Range(0.0f, 1.0f), Random.Range(0.0f, 1.0f), Random.Range(0.0f, 1.0f));
                    cube.GetComponent<Renderer>().material.shader = Shader.Find("Transparent/Diffuse");
                    material.Add(cube);
                }
            }

        }
        yield return new WaitForSeconds(1);
    }
    // Update is called once per frame
    public float i = 0.0f;
    public float j = 1.0f;
    public float k = -10.0f;
    void Update()
    {
        
        StartCoroutine(TestCoroutine());
        Camera mycam = GetComponent<Camera>();
        if (Input.GetKeyDown(KeyCode.RightArrow))
        {
            i += 1.0f;
            mycam.transform.position = new Vector3(i, j,k);
        }
        if (Input.GetKeyDown(KeyCode.LeftArrow))
        {
            i -= 1.0f;
            mycam.transform.position = new Vector3(i, j, k);
        }
        if (Input.GetKeyDown(KeyCode.DownArrow))
        {
            j -= 1.0f;
            mycam.transform.position = new Vector3(i, j, k);
        }
        if (Input.GetKeyDown(KeyCode.UpArrow))
        {
            j += 1.0f;
            mycam.transform.position = new Vector3(i, j, k);
        }
        if (Input.GetKeyDown(KeyCode.Z))
        {
            k -= 1.0f;
            mycam.transform.position = new Vector3(i, j, k);
        }
        if (Input.GetKeyDown(KeyCode.X))
        {
            k += 1.0f;
            mycam.transform.position = new Vector3(i, j, k);
        }
        if (Input.GetKeyDown(KeyCode.Mouse0))
        {
            float x = 5 * Input.mousePosition.x / 10000;
            float y = 5 * -Input.mousePosition.y / 10000;
            float z = 5 * Input.mousePosition.z / 10000;
            mycam.transform.Rotate(x, y, z);
        }
    }
}

