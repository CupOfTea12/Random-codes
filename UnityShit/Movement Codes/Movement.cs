using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{
    public float speed ;
    public float rotationSpeed ;
    private Animator animator;
    
    void Start(){
     animator = GetComponent<Animator>();

    }

    // Update is called once per frame
    void Update()
    {
        float xDirection = Input.GetAxisRaw("Vertical");
        float zDirection = Input.GetAxisRaw("Horizontal");

        Vector3 moveDirection = new Vector3(xDirection, 0, zDirection);
       // float magnitude = Mathf.Clamp01(moveDirection.magnitude)*speed;
       moveDirection.Normalize();
       transform.Translate(moveDirection * speed * Time.deltaTime, Space.World );
      
      if(moveDirection != Vector3.zero){
       // transform.forward = moveDirection;
       animator.SetBool("isMoving",true);
       Quaternion toRotation = Quaternion.LookRotation(moveDirection, Vector3.up);
       transform.rotation = Quaternion.RotateTowards(transform.rotation, toRotation, rotationSpeed * Time.deltaTime);
      }else{
               animator.SetBool("isMoving",false);

      }
    }
}
